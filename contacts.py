import json

FILE = "contacts.json"

try:
    with open(FILE, "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = []

def save():
    with open(FILE, "w") as f:
        json.dump(contacts, f)

def view():
    if len(contacts) == 0:
        print("No contacts yet.")
    for i, c in enumerate(contacts, start=1):
        print(i, c["name"], "|", c["phone"], "|", c["email"])

while True:
    print("\n1. Add  2. View  3. Edit  4. Delete  5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        save()
        print("Contact added!")
    elif choice == "2":
        view()
    elif choice == "3":
        view()
        n = int(input("Number to edit: "))
        contacts[n-1]["name"] = input("New name: ")
        contacts[n-1]["phone"] = input("New phone: ")
        contacts[n-1]["email"] = input("New email: ")
        save()
        print("Contact updated!")
    elif choice == "4":
        view()
        n = int(input("Number to delete: "))
        contacts.pop(n-1)
        save()
        print("Contact deleted!")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")