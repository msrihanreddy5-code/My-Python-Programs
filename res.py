# Restaurant Management System
# Features: Add Menu Items, Edit Menu Items, View All Items, Delete Items, Generate Bill, Search Item, Exit

menu = {}

def add_item():
    name = input("Enter dish name: ").lower()
    if name in menu:
        print("Dish already exists in the menu!")
        return
    try:
        price = float(input("Enter price: "))
        category = input("Enter category (Starter/Main/Dessert/Drink): ")
        menu[name] = {"price": price, "category": category}
        print(f"Dish '{name}' added successfully to the menu.")
    except ValueError:
        print("Invalid price input.")

def edit_item():
    name = input("Enter dish name to edit: ").lower()
    if name not in menu:
        print("Dish not found in the menu!")
        return
    try:
        price_input = input("Enter new price (leave blank to keep current): ")
        if price_input:
            menu[name]['price'] = float(price_input)
        
        category_input = input("Enter new category (leave blank to keep current): ")
        if category_input:
            menu[name]['category'] = category_input
            
        print(f"Dish '{name}' updated successfully.")
    except ValueError:
        print("Invalid input.")

def view_all_items():
    if not menu:
        print("Menu is empty.")
        return
    print("\n--- Restaurant Menu ---")
    print(f"{'Name':<20} {'Category':<15} {'Price':<10}")
    print("-" * 45)
    for name, details in menu.items():
        print(f"{name.capitalize():<20} {details['category']:<15} ${details['price']:<10.2f}")

def delete_item():
    name = input("Enter dish name to delete: ").lower()
    if name in menu:
        del menu[name]
        print(f"Dish '{name}' removed from the menu.")
    else:
        print("Dish not found.")

def generate_bill():
    if not menu:
        print("Menu is empty. Cannot generate bill.")
        return
    
    order_items = []
    total = 0.0
    
    print("\n--- Order Entry ---")
    while True:
        name = input("Enter dish name (or 'done' to finish): ").lower()
        if name == 'done':
            break
        if name not in menu:
            print("Dish not found in menu.")
            continue
        try:
            qty = int(input(f"Enter quantity for {name.capitalize()}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
                
            cost = menu[name]['price'] * qty
            total += cost
            order_items.append({"name": name, "qty": qty, "price": menu[name]['price'], "cost": cost})
        except ValueError:
            print("Invalid quantity.")
    
    if order_items:
        print("\n" + "="*30)
        print("      RESTAURANT BILL")
        print("="*30)
        for item in order_items:
            print(f"{item['name'].capitalize():<15} x{item['qty']:<3} ${item['cost']:>8.2f}")
        print("-" * 30)
        print(f"{'TOTAL:':<20} ${total:>8.2f}")
        print("="*30)
        print("   Thank you for dining!")
        print("="*30)

def search_element():
    name = input("Enter dish name to search: ").lower()
    if name in menu:
        details = menu[name]
        print(f"Found: {name.capitalize()} | Category: {details['category']} | Price: ${details['price']:.2f}")
    else:
        print("Dish not found in the menu.")

def main():
    while True:
        print("\n--- RESTAURANT MANAGEMENT SYSTEM ---")
        print("1. Add Menu Items")
        print("2. Edit Menu Items")
        print("3. View All Items")
        print("4. Delete Items")
        print("5. Generate Bill")
        print("6. Search Item")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            edit_item()
        elif choice == '3':
            view_all_items()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            generate_bill()
        elif choice == '6':
            search_element()
        elif choice == '7':
            print("Exiting Restaurant System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
