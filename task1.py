
import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    if not name or not phone:
        print("Name and phone number are required.")
        return
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter contact name to update: ").strip()
    if name in contacts:
        new_phone = input("Enter new phone number: ").strip()
        if new_phone:
            contacts[name] = new_phone
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully.")
        else:
            print("Phone number cannot be empty.")
    else:
        print("Contact not found.")
def main():
    """Main function to drive the contact management system."""
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
