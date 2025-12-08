print("--- Unit Converter ---")
print("1. cm → m")
print("2. cm → km")
print("3. m → cm")
print("4. km → m")

choice = int(input("Choose option: "))
value = float(input("Enter value: "))

if choice == 1:
    print(value / 100, "meters")
elif choice == 2:
    print(value / 100000, "kilometers")
elif choice == 3:
    print(value * 100, "centimeters")
elif choice == 4:
    print(value * 1000, "meters")
else:
    print("Invalid choice")
