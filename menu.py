from manager import add_contact, view_contact,remove_contact,search_contact


while True:
    print("\n\n Welcome to  CONTACT MANAGEMENT APP ")
    print(" 1. Add Contact: ")
    print(" 2. View Contact: ")
    print(" 3. Remove Contact: ")
    print(" 4. Search Contact: ")
    print(" 5. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        first_name=input("Enter your first name: ")
        last_name=input("Enter your last name: ")
        email=input("Enter email Adress: ")
        contact_no=input("Enter Contact Number: ")
        adress=input("Enter your adress: ")
        add_contact(first_name,last_name,email,contact_no,adress)
        print("Task added Successfully!")
    
    elif choice == "2":
        view_contact()
    elif choice == "3":
        index=int(input("Enter the contact indext to remove: "))
        remove_contact(index)
    elif choice == "4":
        query= input("Enter the search query: ")
        print("\nSearch Results: ")
        search_contact(query)
        
    elif choice == "5":
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and terminate the program
    else:
     print("Invalid choice. Please try again.")
    