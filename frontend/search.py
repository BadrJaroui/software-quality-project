from database.methods import DatabaseManager

def search_scooter_ui():
    db = DatabaseManager("database/data/urban_mobility.db")

    while True:
        print("Search on:\n1. ID\n2. serial number")
        user_input = input()
        scooter = None

        if user_input == "1":
            print("Type an ID:")
            id = input()
            scooter = db.search_scooter(id, None)
        elif user_input == "2":
            print("Type a serial number:")
            serial = input()
            scooter = db.search_scooter(None, serial)

        if not scooter == None:
            print(scooter)
            break
        else:
            print("Scooter does not exist.")
            break

def search_traveller_ui():
    db = DatabaseManager("database/data/urban_mobility.db")

    while True:
        print("Search traveller by:\n1. ID\n2. First name\n3. Last name\n4. Email address")
        user_input = input("Your choice: ")
        traveller = None

        if user_input == "1":
            id = input("Enter ID: ")
            traveller = db.search_traveller(id=id)
        elif user_input == "2":
            first_name = input("Enter first name: ")
            traveller = db.search_traveller(first_name=first_name)
        elif user_input == "3":
            last_name = input("Enter last name: ")
            traveller = db.search_traveller(last_name=last_name)
        elif user_input == "4":
            email = input("Enter email address: ")
            traveller = db.search_traveller(email_address=email)
        else:
            print("Invalid option.")
            continue

        if traveller is not None:
            print("Traveller found:")
            print(traveller)
            break
        else:
            print("Traveller not found.")
            break