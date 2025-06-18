from database.methods import DatabaseManager
from security.security import hash_password, check_password, validate_password, validate_username
from utils.utils import update_password
from utils.utils import get_role_by_id
from utils.CurrentLoggedInUser import currentUserID

def update_traveller():
    db = DatabaseManager("database/data/urban_mobility.db")

    traveller_id = input("Enter the ID of the traveller to update: ")

    print("Enter new values (leave blank to skip updating a field):")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birthday = input("Birthday: ")
    gender = input("Gender: ")
    zipcode = input("Zipcode: ")
    city = input("City: ")
    email = input("Email: ")
    number = input("Phone number: ")
    license_number = input("License number: ")

    updates = {}
    if first_name: updates["first_name_enc"] = first_name
    if last_name: updates["last_name_enc"] = last_name
    if birthday: updates["birthday_enc"] = birthday
    if gender: updates["gender_enc"] = gender
    if zipcode: updates["zipcode_enc"] = zipcode
    if city: updates["city_enc"] = city
    if email: updates["email_enc"] = email
    if number: updates["number_enc"] = number
    if license_number: updates["license_number_enc"] = license_number

    if updates:
        db.update_traveller(int(traveller_id), **updates)
        print("Traveller updated successfully!")
    else:
        print("No updates provided.")

def update_scooter():
    db = DatabaseManager("database/data/urban_mobility.db")
    scooter_id = input("Enter the ID of the scooter to update: ")

    print("Enter new values (leave blank to skip updating a field):")

    brand = model = serial_number = top_speed = battery_capacity = None
    if get_role_by_id(currentUserID).lower() == "system admin" or get_role_by_id(currentUserID).lower() == "super admin":
        brand = input("Brand: ")
        model = input("Model: ")
        serial_number = input("Serial number: ")
        top_speed = input("Top speed: ")
        battery_capacity = input("Battery capacity: ")

    state_of_charge = input("State of charge: ")
    target_range = input("Target range: ")
    location = input("Location: ")
    out_of_service_status = input("Out-of-service status: ")
    mileage = input("Mileage: ")
    last_maintenance_date = input("Last maintenance date: ")

    updates = {}
    if brand: updates["brand"] = brand
    if model: updates["model"] = model
    if serial_number: updates["serial_number"] = serial_number
    if top_speed: updates["top_speed"] = float(top_speed)
    if battery_capacity: updates["battery_capacity"] = float(battery_capacity)
    if state_of_charge: updates["state_of_charge"] = float(state_of_charge)
    if target_range: updates["target_range_soc"] = target_range
    if location: updates["location_enc"] = location
    if out_of_service_status: updates["out_of_service_status"] = int(out_of_service_status)
    if mileage: updates["mileage"] = float(mileage)
    if last_maintenance_date: updates["last_maintenance_date"] = last_maintenance_date

    if updates:
        db.update_scooter(int(scooter_id), **updates)
        print("Scooter updated successfully!")
    else:
        print("No updates provided.")

def update_user():
    db = DatabaseManager("database/data/urban_mobility.db")
    user_id = input("Enter the ID of the user to update: ")

    print("Enter new values (leave blank to skip updating a field):")
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role: ")
    first_name = input("First name: ")
    last_name = input("Last name: ")

    updates = {}

    if username:
        valid, message = validate_username(username)
        if not valid:
            print(f"Username not valid: {message}")
            return
        updates["username"] = username

    if password:
        valid, message = validate_password(password)
        if not valid:
            print(f"Password not valid: {message}")
            return
        updates["password_hash"] = hash_password(password)

    if role:
        updates["role"] = role
    if first_name:
        updates["first_name"] = first_name
    if last_name:
        updates["last_name"] = last_name

    if updates:
        db.update_user(int(user_id), **updates)
        print("User updated successfully!")
    else:
        print("No updates provided.")

def update_password_ui():
    db = DatabaseManager("database/data/urban_mobility.db")
    current_user = db.search_user(id=currentUserID)

    current_pass = current_user[0][2]

    while True:
        print("Enter a new password:")
        new_pass = input()
        if not validate_password(new_pass):
            print("This is not a valid password.")
            continue

        elif check_password(new_pass, current_pass):
            print("This password is already being used. Please use a new password.")
            continue

        else:
            update_password(currentUserID, hash_password(new_pass))
            print("Password has been updated.")
            break