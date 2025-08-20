class Contact:
    def init(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

head = None

def add_contact():
    global head
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    new_contact = Contact(name, phone)
    new_contact.next = head
    head = new_contact
    print("Contact added!\n")

def view_contacts():
    temp = head
    if temp is None:
        print("No contacts found!\n")
        return
    print("\n--- All Contacts ---")
    while temp:
        print(f"Name: {temp.name}, Phone: {temp.phone}")
        temp = temp.next
    print()

def search_contact():
    temp = head
    target = input("Enter name to search: ")
    while temp:
        if temp.name.lower() == target.lower():
            print(f"Found: {temp.name} - {temp.phone}\n")
            return
        temp = temp.next
    print("Contact not found!\n")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        ch = int(input("Choice: "))
        
        if ch == 1:
            add_contact()
        elif ch == 2:
            view_contacts()
        elif ch == 3:
            search_contact()
        elif ch == 4:
            break
        else:
            print("Invalid choice!\n")

if name == "main":
    main()
