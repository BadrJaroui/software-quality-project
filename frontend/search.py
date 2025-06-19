from database.methods import DatabaseManager
from security.security import decrypt_scooter_data, decrypt_traveller_data

def search_scooter_ui():
    db = DatabaseManager("database/data/urban_mobility.db")

    while True:
        print("Search on:\n1. ID\n2. Serial Number")
        user_input = input()
        scooter = None

        if user_input == "1":
            print("Type an ID:")
            id = input()
            scooter = db.search_scooter(id, None)
        elif user_input == "2":
            print("Type a Serial Number:")
            serial = input()
            scooter = db.search_scooter(None, serial)

        if scooter is not None:
            decrypted_scooter = decrypt_scooter_data(scooter)
            print(decrypted_scooter)
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
            decrypted_traveller = decrypt_traveller_data(traveller)
            print("Traveller found:")
            print(decrypted_traveller)
            break
        else:
            print("Traveller not found.")
            break