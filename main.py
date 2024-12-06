import csv, os

def load_contacts():
    if not os.path.exists('contact.csv'):
        return []
    with open('contact.csv', 'r') as file:
            f = csv.DictReader(file)
            return [row for row in f]

def save(contactbook):
    with open('contact.csv', 'w', newline='') as file:
        fields = ['name', 'email', 'contact_no', 'address']
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(contactbook)

def add_contact(name, email, contact_no, address):
    contactbook = load_contacts()

    for contact in contactbook:
        if contact['contact_no'] == contact_no:
            print("Contact already found!")
            return

    new_contact = {
        'name'      : name,
        'email'     : email,
        'contact_no': contact_no,
        'address'   : address
    }
    contactbook.append(new_contact)
    save(contactbook)

def remove_contact(contact_no):
    contactbook = load_contacts()
    delete_contact = None
    for contact in contactbook:
        if contact['contact_no'] == contact_no:
            delete_contact = contact

    if delete_contact:
        contactbook.remove(delete_contact)
        save(contactbook)
        print("Contact deleted")
    else:
        print("Contact Not found")

def search_contact(name):
    contactbook = load_contacts()
    result = []

    for contact in contactbook:
        if contact['name'] == name:
            result.append(contact)

    if result:
        print("## Search Results:\n")
        for i, contact in enumerate(result, start=1):
            print(
                f"{i}. Name: {contact['name']}, Email: {contact['email']}, "
                f"Contact No: {contact['contact_no']}, Address: {contact['address']}"
            )
    else:
        print("Name not found")

def view_contact():
    contactbook = load_contacts()
    print("####Contact lists####\n")
    for i, contact in enumerate(contactbook, start=1):
        print(
            f"{i}. Name: {contact['name']}, Email: {contact['email']}, "
            f"Contact No: {contact['contact_no']}, Address: {contact['address']}"
        )


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
