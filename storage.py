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
