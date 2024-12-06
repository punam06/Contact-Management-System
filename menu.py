from manager import add_contact,view_contact,remove_contact,search_contact

def menu():
    while True:
        print("\n\nWelcome to CONTACT MANAGEMENT APP")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                contact_no = input("Enter contact number: ").strip()
                address = input("Enter your address: ").strip()

                # Validate that all fields are filled
                if not name or not email or not contact_no or not address:
                    raise ValueError("All fields must be filled out.")

                add_contact(name, email, contact_no, address)
                print("Task added successfully!")

            except ValueError as ve:
                print(f"Input Error: {ve}")

        elif choice == "2":
            view_contact()

        elif choice == "3":
            try:
                name = input("Enter the name of the contact to remove: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty.")
                remove_contact(name)

            except ValueError as ve:
                print(f"Input Error: {ve}")

        elif choice == "4":
            try:
                query = input("Enter the search query: ").strip()
                if not query:
                    raise ValueError("Search query cannot be empty.")
                search_contact(query)

            except ValueError as ve:
                print(f"Input Error: {ve}")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
