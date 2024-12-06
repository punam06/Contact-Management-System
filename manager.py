from storage import save,load_contacts


def add_contact(name, email, contact_no, address):
    contactbook = load_contacts()

    for contact in contactbook:
        if contact['contact_no'] == contact_no:
            print("Contact already found!")
            return

    new_contact = {
        'name'      : name,
        'email'     : email,
        'contact_no'   : contact_no,
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
