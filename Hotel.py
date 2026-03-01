import os

class HotelManagement:
    def __init__(self):
        self.rooms = {
            "101": {"type": "Single", "price": 5000, "vacant": True},
            "102": {"type": "Double", "price": 8000, "vacant": True},
            "201": {"type": "Suite", "price": 15000, "vacant": True},
            "202": {"type": "Suite", "price": 15000, "vacant": True},
        }
        self.bookings = []
        self.food_menu = [
            {"name": "Club Sandwich", "price": 800},
            {"name": "Caesar Salad", "price": 600},
            {"name": "Tomato Soup", "price": 500},
            {"name": "Chocolate Cake", "price": 700},
        ]

    def display_menu(self):
        print("\n--- Hotel Management System ---")
        print("1. View Rooms")
        print("2. Book a Room (Entry)")
        print("3. View Food Menu")
        print("4. View Vacant Rooms")
        print("5. Checkout (Exit)")
        print("6. Exit Program")

    def view_rooms(self):
        print("\n--- All Rooms ---")
        for r_no, details in self.rooms.items():
            status = "Vacant" if details["vacant"] else "Occupied"
            print(f"Room {r_no}: {details['type']} | Price: {details['price']} | Status: {status}")

    def book_room(self):
        self.view_vacant_rooms()
        room_no = input("\nEnter Room Number to book: ")
        if room_no in self.rooms and self.rooms[room_no]["vacant"]:
            guest_name = input("Enter Guest Name: ")
            self.rooms[room_no]["vacant"] = False
            self.bookings.append({"room": room_no, "guest": guest_name})
            print(f"Room {room_no} successfully booked for {guest_name}.")
        else:
            print("Invalid Room Number or Room already occupied.")

    def view_food_menu(self):
        print("\n--- Food Menu ---")
        for item in self.food_menu:
            print(f"{item['name']}: {item['price']}")

    def view_vacant_rooms(self):
        print("\n--- Vacant Rooms ---")
        found = False
        for r_no, details in self.rooms.items():
            if details["vacant"]:
                print(f"Room {r_no}: {details['type']} | Price: {details['price']}")
                found = True
        if not found:
            print("No vacant rooms available.")

    def checkout(self):
        room_no = input("\nEnter Room Number for checkout: ")
        if room_no in self.rooms and not self.rooms[room_no]["vacant"]:
            self.rooms[room_no]["vacant"] = True
            print(f"Checkout successful for Room {room_no}. Room is now vacant.")
        else:
            print("Invalid Room Number or Room is already vacant.")

def main():
    hotel = HotelManagement()
    while True:
        hotel.display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            hotel.view_rooms()
        elif choice == "2":
            hotel.book_room()
        elif choice == "3":
            hotel.view_food_menu()
        elif choice == "4":
            hotel.view_vacant_rooms()
        elif choice == "5":
            hotel.checkout()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
