import json
import os
import csv  # Import csv for handling CSV files

def save_contact(contacts):
    # Save contacts to JSON file
    with open('contact.json', 'w') as file:
        json.dump(contacts, file, indent=4)

    # Save contacts to CSV file
    with open('contact.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'email', 'contact_no', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header
        for contact in contacts:
            writer.writerow(contact)  # Write each contact as a row

def load_contact():
    if not os.path.exists('contact.json'):
        return []  # Return an empty list if the file does not exist

    with open('contact.json', 'r') as file:
        return json.load(file)

def load_contact_csv():
    if not os.path.exists('contact.csv'):
        return []  # Return an empty list if the CSV file does not exist

    with open('contact.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]  # Return a list of dictionaries
