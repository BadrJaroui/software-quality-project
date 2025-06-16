from database_stuff.DBOperations import update_traveller

def update_traveller_ui():
    id = input("Enter the traveller ID you want to update: ")

    fields = {
        "1": "FirstName",
        "2": "LastName",
        "3": "Birthday",
        "4": "Gender",
        "5": "ZipCode",
        "6": "City",
        "7": "EmailAddress",
        "8": "MobilePhone",
        "9": "LicenseNumber"
    }

    updates = {}

    print("\nSelect fields to update (type the number, or 'done' to finish):")

    for key, value in fields.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Field number to update (or 'done'): ").strip()

        if choice.lower() == "done":
            break

        if choice in fields:
            new_value = input(f"Enter new value for {fields[choice]}: ")
            updates[fields[choice]] = new_value
        else:
            print("Invalid choice, try again.")

    if not updates:
        print("No updates provided.")
        return

    confirm = input("Confirm update? (y/n): ").lower()
    if confirm == 'y':
        update_traveller(id, updates)
    else:
        print("Update canceled.")