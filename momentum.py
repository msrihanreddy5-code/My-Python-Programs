import yfinance as yf
import pandas as pd
import numpy as np
import ta
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
STOCKS = [
    'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
    'BHARTIARTL.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'HCLTECH.NS', 'MARUTI.NS'
]
START_DATE = '2015-01-01'
END_DATE = '2025-12-31'
TRAIN_END_DATE = '2022-12-31'
TEST_START_DATE = '2023-01-01'
TRANSACTION_COST = 0.001  # 10 bps (0.1%)

def fetch_data(tickers, start, end):
    print("Fetching data...")
    data = yf.download(tickers, start=start, end=end, group_by='ticker', auto_adjust=True)
    return data

def calculate_technical_indicators(df):
    df = df.copy()
    if 'Close' not in df.columns:
         df.columns = [c.capitalize() for c in df.columns]

    # Fill missing values first
    df = df.ffill().bfill()

    # RSI
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    
    # MACD
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    
    # Bollinger Bands
    bollinger = ta.volatility.BollingerBands(df['Close'])
    df['BB_High'] = bollinger.bollinger_hband()
    df['BB_Low'] = bollinger.bollinger_lband()
    
    # ATR
    df['ATR'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close']).average_true_range()
    
    # SMA / EMA
    df['SMA_50'] = ta.trend.SMAIndicator(df['Close'], window=50).sma_indicator()
    df['EMA_20'] = ta.trend.EMAIndicator(df['Close'], window=20).ema_indicator()
    
    # Returns for features
    df['Return_1W'] = df['Close'].pct_change(5)
    df['Return_1M'] = df['Close'].pct_change(21)
    
    # Volatility
    df['Volatility_1M'] = df['Close'].rolling(window=21).std()
    
    return df

def prepare_weekly_data(data):
    print("Preparing weekly aligned data...")
    weekly_data = []
    
    for ticker in STOCKS:
        try:
            df = data[ticker].copy()
        except KeyError:
             if len(STOCKS) == 1: df = data.copy()
             else: continue
        
        df = df.dropna(how='all')
        df = calculate_technical_indicators(df)
        
        # Resample to weekly (Mondays)
        # Logic:
        # 1. Identify Mondays (or first trading day of week)
        # 2. Features = Values from previous trading day (Friday)
        # 3. Target = Return from this Monday to Next Monday
        
        # Create a 'Week_Start' column
        df['Date'] = df.index
        df['Week_Start'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)
        
        # We want to trade on the first day of the week.
        # Let's get the data for each week.
        # We'll group by Week_Start and take the first and last available day prices?
        # Better: Resample to Weekly.
        
        # Resample to Weekly, taking the LAST value of the week (Friday)
        # This gives us the features at the end of the week.
        # We will use these features to predict the return of the NEXT week.
        # Trade logic: Enter on Monday Open (approx by Friday Close or Monday Close?), Hold till next Monday.
        # Let's assume we trade on Monday Close.
        # Features: Friday Close (t-1).
        # Trade: Monday Close (t).
        # Return: (Next Monday Close (t+5) / Monday Close (t)) - 1.
        
        # Actually, simpler approach:
        # Use Weekly Resampled Data (Friday to Friday).
        # Predict if Next Week (Fri to Fri) is positive.
        # Trade on Friday Close?
        # The prompt says "Rebalance on Mondays".
        
        # Strict implementation of "Rebalance on Mondays":
        # 1. Get all dates. Filter for Mondays (or first day of week).
        # 2. For each Monday date `d`:
        #    - Features: Data from `d-1` (Friday).
        #    - Buy Price: Close of `d`.
        #    - Sell Price: Close of `next Monday`.
        
        # Let's build a DataFrame of "Trading Weeks".
        # We need a custom calendar.
        
        df['DayOfWeek'] = df.index.dayofweek
        # 0=Mon, 4=Fri
        
        # Filter for Rebalance Days (Mondays or first available)
        # We can use `resample('W-MON')` to get the dates, then find nearest valid date?
        
        # Let's iterate through the daily dataframe
        # Identify "Rebalance Days"
        
        # Create a list of rebalance dates
        # We can just take the first date of each week in the dataset
        df['YearWeek'] = df.index.strftime('%Y-%U')
        rebalance_dates = df.groupby('YearWeek')['Date'].min().sort_values()
        
        rebalance_df = pd.DataFrame({'Rebalance_Date': rebalance_dates})
        rebalance_df['Ticker'] = ticker
        
        # Get Features from the day BEFORE Rebalance_Date
        # We need to look up the index in the original df
        
        features_list = []
        targets_list = []
        
        for i in range(len(rebalance_dates) - 1):
            curr_date = rebalance_dates.iloc[i]
            next_date = rebalance_dates.iloc[i+1]
            
            # Find index of curr_date in df
            try:
                curr_idx_loc = df.index.get_loc(curr_date)
            except KeyError:
                continue
                
            if curr_idx_loc == 0:
                continue
                
            # Features from previous day (Friday)
            prev_day_idx = curr_idx_loc - 1
            prev_day_row = df.iloc[prev_day_idx]
            
            # Target: Return from curr_date to next_date
            # Buy at Close of curr_date
            buy_price = df.loc[curr_date, 'Close']
            sell_price = df.loc[next_date, 'Close']
            
            weekly_return = (sell_price / buy_price) - 1
            target = 1 if weekly_return > 0 else 0
            
            # Collect features
            feat_row = prev_day_row[['RSI', 'MACD', 'MACD_Signal', 'BB_High', 'BB_Low', 'ATR', 
                                     'SMA_50', 'EMA_20', 'Return_1W', 'Return_1M', 'Volatility_1M']].to_dict()
            feat_row['Date'] = curr_date
            feat_row['Ticker'] = ticker
            feat_row['Target'] = target
            feat_row['Weekly_Return'] = weekly_return
            
            features_list.append(feat_row)
            
        stock_weekly_df = pd.DataFrame(features_list)
        weekly_data.append(stock_weekly_df)
        
    full_weekly_df = pd.concat(weekly_data)
    full_weekly_df = full_weekly_df.dropna()
    return full_weekly_df

def train_model(train_df):
    print("Training model...")
    feature_cols = ['RSI', 'MACD', 'MACD_Signal', 'BB_High', 'BB_Low', 'ATR', 
                    'SMA_50', 'EMA_20', 'Return_1W', 'Return_1M', 'Volatility_1M']
    
    X = train_df[feature_cols]
    y = train_df['Target']
    
    # Voting Classifier
    clf1 = RandomForestClassifier(n_estimators=100, random_state=42)
    clf2 = LogisticRegression(random_state=42, max_iter=1000)
    clf3 = GradientBoostingClassifier(n_estimators=100, random_state=42)
    
    eclf = VotingClassifier(estimators=[('rf', clf1), ('lr', clf2), ('gb', clf3)], voting='soft')
    eclf.fit(X, y)
    
    print("Training Accuracy:", eclf.score(X, y))
    return eclf, feature_cols

def backtest(model, test_df, feature_cols):
    print("Running backtest...")
    # Predict probabilities
    X_test = test_df[feature_cols]
    test_df['Prob_Positive'] = model.predict_proba(X_test)[:, 1]
    
    # Group by Date (Rebalance Date)
    dates = test_df['Date'].unique()
    dates = np.sort(dates)
    
    portfolio_returns = []
    portfolio_values = [10000] # Start with 10k
    
    records = []

    for date in dates:
        # Get stocks for this week
        weekly_slice = test_df[test_df['Date'] == date]
        
        # Rank by Probability
        weekly_slice = weekly_slice.sort_values(by='Prob_Positive', ascending=False)
        
        # Select Top 2
        top_picks = weekly_slice.head(2)
        
        if len(top_picks) == 0:
            portfolio_returns.append(0)
            continue
            
        # Equal Weight (50% each)
        # Return for this week is average of selected stocks' returns
        # Apply Transaction Cost: 0.1% entry + 0.1% exit = 0.2% total per trade?
        # Yes, "10 basis points (0.1%) per side". Total 0.2% per trade cycle.
        
        raw_return = top_picks['Weekly_Return'].mean()
        net_return = raw_return - (TRANSACTION_COST * 2) # Buy and Sell
        
        portfolio_returns.append(net_return)
        
        # Update Portfolio Value
        current_val = portfolio_values[-1] * (1 + net_return)
        portfolio_values.append(current_val)
        
        # Record picks
        for _, row in top_picks.iterrows():
            records.append({
                'Date': date,
                'Ticker': row['Ticker'],
                'Prob': row['Prob_Positive'],
                'Weight': 0.5,
                'Return': row['Weekly_Return']
            })
            
    results_df = pd.DataFrame({
        'Date': dates,
        'Weekly_Return': portfolio_returns,
        'Portfolio_Value': portfolio_values[1:] # Align length
    })
    
    picks_df = pd.DataFrame(records)
    
    return results_df, picks_df

def calculate_metrics(results_df):
    # Daily/Weekly metrics
    # We have weekly returns
    
    returns = results_df['Weekly_Return']
    
    # Annualized Return
    # (1 + total_return)^(52 / n_weeks) - 1
    total_return = (results_df['Portfolio_Value'].iloc[-1] / 10000) - 1
    n_weeks = len(results_df)
    annualized_return = (1 + total_return) ** (52 / n_weeks) - 1
    
    # Annualized Volatility
    # std_dev * sqrt(52)
    annualized_vol = returns.std() * np.sqrt(52)
    
    # Sharpe Ratio
    # (Ann_Ret - RiskFree) / Ann_Vol. Assume RF=0 for simplicity or 5%?
    # Let's use 0 as standard if not specified, or small number.
    sharpe_ratio = annualized_return / annualized_vol if annualized_vol != 0 else 0
    
    # Max Drawdown
    cum_returns = (1 + returns).cumprod()
    peak = cum_returns.cummax()
    drawdown = (cum_returns - peak) / peak
    max_drawdown = drawdown.min()
    
    metrics = {
        'Total Return': total_return,
        'Annualized Return': annualized_return,
        'Annualized Volatility': annualized_vol,
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown
    }
    
    return metrics

if __name__ == "__main__":
    # 1. Fetch Data
    raw_data = fetch_data(STOCKS, START_DATE, END_DATE)
    
    # 2. Prepare Weekly Data
    full_df = prepare_weekly_data(raw_data)
    
    # 3. Split Train/Test
    # Train: 2015-2022
    # Test: 2023-2025
    
    train_df = full_df[full_df['Date'] <= TRAIN_END_DATE]
    test_df = full_df[full_df['Date'] >= TEST_START_DATE]
    
    print(f"Train size: {len(train_df)}, Test size: {len(test_df)}")
    
    # 4. Train Model
    model, features = train_model(train_df)
    
    # 5. Backtest
    results, picks = backtest(model, test_df, features)
    
    # 6. Metrics
    metrics = calculate_metrics(results)
    print("Performance Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v:.4f}")
        
    # 7. Save Outputs
    os.makedirs("outputs", exist_ok=True)
    results.to_csv("outputs/portfolio_performance.csv", index=False)
    picks.to_csv("outputs/weekly_picks.csv", index=False)
    
    # 8. Plots
    plt.figure(figsize=(12, 6))
    plt.plot(results['Date'], results['Portfolio_Value'])
    plt.title('Portfolio Equity Curve (2023-2025)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig("outputs/equity_curve.png")
    print("Outputs saved to 'outputs/' directory.")
