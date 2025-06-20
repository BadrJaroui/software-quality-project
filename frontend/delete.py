from database.methods import DatabaseManager
from utils.CurrentLoggedInUser import currentUserID

def delete_traveller():
    db = DatabaseManager("database/data/urban_mobility.db")

    traveller_id = input("Enter the ID of the traveller to delete: ")
    if traveller_id.isdigit():
        db.delete_traveller(int(traveller_id))
        print("Traveller deleted successfully!")
    else:
        print("Invalid ID. Please enter a numeric value.")

def delete_scooter():
    db = DatabaseManager("database/data/urban_mobility.db")

    scooter_id = input("Enter the ID of the scooter to delete: ")
    if scooter_id.isdigit():
        db.delete_scooter(int(scooter_id))
        print("Scooter deleted successfully!")
    else:
        print("Invalid ID. Please enter a numeric value.")

def delete_user():
    db = DatabaseManager("database/data/urban_mobility.db")

    user_id = input("Enter the ID of the user to delete: ")
    if user_id.isdigit():
        db.delete_user(int(user_id))
        print("User deleted successfully!")
    else:
        print("Invalid ID. Please enter a numeric value.")

def delete_restore_code():
    db = DatabaseManager("database/data/urban_mobility.db")

    code_id = input("Enter the ID of the restore code to delete: ")
    if code_id.isdigit():
        db.delete_restore_code(int(code_id))
        print("Restore code deleted successfully!")
    else:
        print("Invalid ID. Please enter a numeric value.")