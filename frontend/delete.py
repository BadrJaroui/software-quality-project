from database.methods import DatabaseManager

def delete_traveller():
    traveller_id = input("Enter the ID of the traveller to delete: ")
    if traveller_id.isdigit():
        DatabaseManager.delete_traveller(int(traveller_id))
        print("Traveller deleted successfully!")
    else:
        print("Invalid ID. Please enter a numeric value.")
