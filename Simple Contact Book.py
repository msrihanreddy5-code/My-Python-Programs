contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added!")

    elif choice == "2":
        print("\nSaved Contacts:")
        for name, number in contacts.items():
            print(name, ":", number)

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("Number:", contacts[search])
        else:
            print("Not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
