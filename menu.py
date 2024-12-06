from manager import add_contact,view_contact,remove_contact,search_contact

def menu():
    while True:
        print("\n\n Welcome to  CONTACT MANAGEMENT APP ")
        print(" 1. Add Contact: ")
        print(" 2. View Contact: ")
        print(" 3. Remove Contact: ")
        print(" 4. Search Contact: ")
        print(" 5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter name : ")
            email = input("Enter email: ")
            contact_no = input("Enter contact number: ")
            address = input("Enter your address: ")
            add_contact(name, email, contact_no, address)
            print("Task added Successfully!")

        elif choice == "2":
            view_contact()
        elif choice == "3":
            name = input("Enter number: ")
            remove_contact(name)
        elif choice == "4":
            query = input("Enter the search query: ")
            search_contact(query)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
