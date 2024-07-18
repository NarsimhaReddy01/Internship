import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Current details: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
