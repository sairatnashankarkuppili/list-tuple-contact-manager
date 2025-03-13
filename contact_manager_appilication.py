contacts = []

def add_contact():
    name = input("\nEnter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    for contact in contacts:
        if contact[0] == name:
            print("Contact with this name already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    print("\nList of Contacts:")
    for contact in contacts:
        print(f"{contact[0]} - {contact[1]} - {contact[2]}")

def search_contact():
    search_name = input("\nEnter name to search: ")
    found = False
    for contact in contacts:
        if contact[0] == search_name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            found = True
            break
    if not found:
        print("Contact not found!")

def update_contact():
    search_name = input("\nEnter name to update: ")
    for i, contact in enumerate(contacts):
        if contact[0] == search_name:
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contacts[i] = (contact[0], new_phone, new_email)
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact():
    search_name = input("\nEnter name to delete: ")
    for i, contact in enumerate(contacts):
        if contact[0] == search_name:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

while True:
    print("\nWelcome to Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
