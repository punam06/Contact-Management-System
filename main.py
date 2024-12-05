

#manger system
def add_contact(first_name,last_name,email,contact_no,adress):
    contacts= load_contact()
    contact={
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'contact_no':contact_no,
        'adress':adress    
    }
    contacts.append(contact)
    save_contact(contacts)
    
def view_contact():
    contacts = load_contact()
    for i, contact in enumerate(contacts,start= 1):
        print(f"{i}First_name:{contact['first_name']}, Last_name:{contact['last_name']},Email:{contact['email']},Contact_no:{contact['contact-no']},Adress:{contact['adress']}")
        


def remove_contact(index):
    contacts = load_contact()
    if 0<index<= len(contacts):
        del contacts[index-1]
        save_contact(contacts)
    else:
        print("Invalid index")
        

def search_contact(query):
    contacts=load_contact()
    result=[]
    for i, contact in contacts:
        if query.lower() in contact['first_name'] or query.lower() in contact ['last_name'] or query in contact ['contact_no']:
            result.append(contact)
    print(f"{i}First_name:{contact['first_name']}, Last_name:{contact['last_name']},Email:{contact['email']},Contact_no:{contact['contact_no']},Adress:{contact['adress']}")
        

#storage and memory
""""
def save_contact(contacts):
    with open('contact.json','w')as file:
        json.dump(contacts, file,indent=4)
def load_contact():
    with open('contact.json','r') as file:
        return json.load(file)
"""
import json
import os
import csv  # Import csv module for CSV file handling

# Function to create the JSON file if it doesn't exist
def create_json_file():
    if not os.path.exists('contact.json'):
        with open('contact.json', 'w') as file:
            json.dump([], file)  # Create an empty JSON array

# Function to create the CSV file if it doesn't exist
def create_csv_file():
    if not os.path.exists('contacts.csv'):
        with open('contacts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['first_name', 'last_name', 'email', 'contact_no', 'adress'])  # Write header


#home page
while True:
    print("Welcome to contact book mangement system")
    print(" 1. Add Contact")
    print(" 2. View Contact")
    print(" 3. Remove Contact")
    print( " 4. Search Contact")
    print( " 5. Exit ")
    
    choice= input("Enter your choice: ")
    if choice =="1":
        first_name=input("Enter your first name: ")
        last_name= input("Enter your last name: ")
        email= input("Enter email Adress: ")
        contact_no= input("Enter Contact Number: ")
        adress= input("Enter your adress: ")
        add_contact(first_name,last_name,email,contact_no,adress)
        print("Task added successfully!")
        
    elif choice=="2":
        view_contact()
    elif choice== "3":
        index= int(input("Enter the contact index to remove:"))
        remove_contact(index)
        print("Contact removed sucessfully!")
    elif choice== "4":
        query=input("Enter the search query: ")
        print("\nSearch Results: ")
        search_contact(query)
        
    elif choice == "5":
        print("Exiting....")
        break;
    
    else:
        print("Invalid choice. Please try again.")
        
        

