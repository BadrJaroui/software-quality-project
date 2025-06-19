from database.methods import DatabaseManager
from security.security import hash_password, check_password, validate_password, validate_username, encrypt_data, decrypt_data
from security.security import validate_zip_code, validate_mobile_phone, validate_driving_license, validate_serial_number, validate_location, validate_iso_date, validate_city
from utils.utils import update_password
from utils.utils import get_role_by_id
from utils.CurrentLoggedInUser import currentUserID

def update_traveller():
    db = DatabaseManager("database/data/urban_mobility.db")

    traveller_id = input("Enter the ID of the traveller to update: ")

    print("Enter new values (leave blank to skip updating a field):")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birthday = input("Birthday (yyyy-mm-dd): ")
    gender = input("Gender: ")
    street_name = input("Street name: ")
    house_number = input("House number: ")
    zipcode = input("Zipcode: ")
    city = input("City: ")
    email = input("Email: ")
    number = input("Phone number (8 digits): ")
    license_number = input("License number: ")

    updates = {}

    if first_name:
        updates["first_name_enc"] = encrypt_data(first_name)
    if last_name:
        updates["last_name_enc"] = encrypt_data(last_name)
    if birthday:
        valid, msg = validate_iso_date(birthday)
        if not valid:
            print(f"Invalid birthday: {msg}")
        else:
            updates["birthday_enc"] = encrypt_data(birthday)
    if gender:
        updates["gender_enc"] = encrypt_data(gender)
    if street_name:
        updates["street_name_enc"] = encrypt_data(street_name)
    if house_number:
        updates["house_number_enc"] = encrypt_data(house_number)
    if zipcode:
        valid, msg = validate_zip_code(zipcode)
        if not valid:
            print(f"Invalid zipcode: {msg}")
        else:
            updates["zip_code_enc"] = encrypt_data(zipcode)
    if city:
        valid, msg = validate_city(city)
        if not valid:
            print(f"Invalid city: {msg}")
        else:
            updates["email_address_enc"] = encrypt_data(city)
    if email:
        updates["city_enc"] = encrypt_data(city)
    if number:
        valid, msg = validate_mobile_phone(number)
        if not valid:
            print(f"Invalid phone number: {msg}")
        else:
            updates["mobile_phone_enc"] = encrypt_data(number)
    if license_number:
        valid, msg = validate_driving_license(license_number)
        if not valid:
            print(f"Invalid driving license number: {msg}")
        else:
            updates["driving_license_number_enc"] = encrypt_data(license_number)

    if updates:
        db.update_traveller(int(traveller_id), **updates)
    else:
        print("No valid updates provided.")

def update_scooter():
    db = DatabaseManager("database/data/urban_mobility.db")
    scooter_id = input("Enter the ID of the scooter to update: ")

    print("Enter new values (leave blank to skip updating a field):")

    brand = model = serial_number = top_speed = battery_capacity = None
    if get_role_by_id(currentUserID).lower() in ["system admin", "super admin"]:
        brand = input("Brand: ")
        model = input("Model: ")
        serial_number = input("Serial number: ")
        top_speed = input("Top speed: ")
        battery_capacity = input("Battery capacity: ")

    state_of_charge = input("State of charge: ")
    target_range = input("Target range: ")
    location = input("Location (format: lat,lon): ")
    out_of_service_status = input("Out-of-service status: ")
    mileage = input("Mileage: ")
    last_maintenance_date = input("Last maintenance date (yyyy-mm-dd): ")

    updates = {}

    if brand:
        updates["brand"] = brand
    if model:
        updates["model"] = model
    if serial_number:
        valid, msg = validate_serial_number(serial_number)
        if not valid:
            print(f"Invalid serial number: {msg}")
        else:
            updates["serial_number"] = encrypt_data(serial_number)
    if top_speed:
        updates["top_speed"] = top_speed
    if battery_capacity:
        updates["battery_capacity"] = battery_capacity
    if state_of_charge:
        updates["state_of_charge"] = state_of_charge
    if target_range:
        updates["target_range_soc"] = target_range
    if location:
        try:
            lat_str, lon_str = [x.strip() for x in location.split(",")]
            valid, msg = validate_location(lat_str, lon_str)
            if not valid:
                print(f"Invalid location: {msg}")
            else:
                updates["location_enc"] = encrypt_data(location)
        except Exception:
            print("Location must be in 'latitude, longitude' format.")
    if out_of_service_status:
        updates["out_of_service_status"] = out_of_service_status
    if mileage:
        updates["mileage"] = mileage
    if last_maintenance_date:
        valid, msg = validate_iso_date(last_maintenance_date)
        if not valid:
            print(f"Invalid date: {msg}")
        else:
            updates["last_maintenance_date"] = last_maintenance_date

    if updates:
        db.update_scooter(int(scooter_id), **updates)
        print("Scooter updated successfully!")
    else:
        print("No valid updates provided.")

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
        updates["username"] = encrypt_data(username)

    if password:
        valid, message = validate_password(password)
        if not valid:
            print(f"Password not valid: {message}")
            return
        updates["password_hash"] = encrypt_data(hash_password(password))

    if role:
        updates["role"] = role
    if first_name:
        updates["first_name"] = encrypt_data(first_name)
    if last_name:
        updates["last_name"] = encrypt_data(last_name)

    if updates:
        db.update_user(int(user_id), **updates)
    else:
        print("No updates provided.")

def update_password_ui():
    db = DatabaseManager("database/data/urban_mobility.db")
    current_user = db.search_user(id=currentUserID)

    current_pass = current_user[0][2]

    while True:
        print("Enter a new password:")
        new_pass = input()
        valid, msg = validate_password(new_pass)
        if not valid:
            print("This is not a valid password.")
            continue

        elif check_password(new_pass, decrypt_data(current_pass)):
            print("This password is already being used. Please use a new password.")
            continue

        else:
            update_password(currentUserID, hash_password(new_pass))
            print("Password has been updated.")
            break