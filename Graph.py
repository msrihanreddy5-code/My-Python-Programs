import matplotlib.pyplot as plt

print("Which graph do you want to draw?")
print("1. Line Graph")
print("2. Bar Graph")
print("3. Scatter Plot")
print("4. Pie Chart")

choice = int(input("Enter your choice (1-4): "))

# Asking data
x = input("Enter X values separated by space: ").split()
y = input("Enter Y values separated by space: ").split()

# Convert to numbers
x = [float(i) for i in x]
y = [float(i) for i in y]

plt.title("User Generated Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

if choice == 1:
    plt.plot(x, y, marker='o')
    print("Drawing Line Graph...")

elif choice == 2:
    plt.bar(x, y)
    print("Drawing Bar Graph...")

elif choice == 3:
    plt.scatter(x, y)
    print("Drawing Scatter Plot...")

elif choice == 4:
    plt.pie(y, labels=x, autopct='%1.1f%%')
    print("Drawing Pie Chart...")

else:
    print("Invalid choice!")
    exit()

plt.show()
