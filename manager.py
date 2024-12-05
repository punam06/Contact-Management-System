from storage import save_contact, load_contact

def add_contact(full_name, email, contact_no, address):
    contacts = load_contact()  # Load existing contacts

    # Split the full name into first and last names
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Please provide both first and last names.")
        return  # Exit the function if the name is not valid

    first_name = name_parts[0]
    last_name = " ".join(name_parts[1:])  # Join the rest of the name as the last name

    # Check for duplicates
    for contact in contacts:
        if contact['email'] == email or contact['contact_no'] == contact_no:
            print("A contact with this email or contact number already exists.")
            return  # Exit the function if a duplicate is found

    new_contact = {  # Create a new contact dictionary
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'contact_no': contact_no,
        'address': address
    }

    contacts.append(new_contact)  # Append the new contact to the list
    save_contact(contacts)  # Save the updated list of contacts
    print("Contact added successfully!")
    
    
def view_contact():
    contacts = load_contact()  # Load contacts
    print("Contact list:\n")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. First_name: {contact['first_name']}, Last_name: {contact['last_name']}, Email: {contact['email']}, Address: {contact['address']}")
def remove_contact(first_name, last_name, contact_no):
    contacts = load_contact()  # Load existing contacts
    contact_to_remove = None

    # Search for the contact to remove
    for contact in contacts:
        if (contact['first_name'].lower() == first_name.lower() and 
                contact['last_name'].lower() == last_name.lower() and 
                contact['contact_no'] == contact_no):
            contact_to_remove = contact
            break

    if contact_to_remove:
        contacts.remove(contact_to_remove)  # Remove the found contact
        save_contact(contacts)  # Save the updated list of contacts
        print("Contact removed successfully!")
    else:
        print("Contact not found. Please provide a valid first name, last name, and contact number.")


def search_contact(first_name=None, last_name=None, contact_no=None):
    contacts = load_contact()  # Load existing contacts
    results = []

    # Search for contacts based on provided parameters
    for contact in contacts:
        if ((first_name is None or contact['first_name'].lower() == first_name.lower()) and
            (last_name is None or contact['last_name'].lower() == last_name.lower()) and
            (contact_no is None or contact['contact_no'] == contact_no)):
            results.append(contact)

    # Display search results
    if results:
        print("\nSearch Results:\n")
        for i, contact in enumerate(results, start=1):
            print(f"{i}. First Name: {contact['first_name']}, Last Name: {contact['last_name']}, Email: {contact['email']}, Contact No: {contact['contact_no']}, Address: {contact['address']}")
    else:
        print("No contacts found matching the search criteria.")
