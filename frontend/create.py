from database.methods import DatabaseManager
from security.security import (
    hash_password, validate_password, validate_username, encrypt_data,
    validate_zip_code, validate_mobile_phone, validate_driving_license,
    validate_serial_number, validate_location, validate_iso_date, validate_city
)
from datetime import datetime

def add_traveller():
    db = DatabaseManager("database/data/urban_mobility.db")

    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    birthday = input("Enter a birthday (yyyy-mm-dd): ")
    gender = input("Enter a gender: ")
    street_name = input("Enter a street name: ")
    house_number = input("Enter a house number: ")
    zipcode = input("Enter a zipcode: ")
    city = input("Enter a city: ")
    email = input("Enter an email address: ")
    number = input("Enter a phone number (8 digits): ")
    license_number = input("Enter a license number: ")
    registration_date = datetime.now().strftime("%Y-%m-%d")
    
    traveller_data = {}
    valid_input = True

    if first_name:
        traveller_data["first_name_enc"] = encrypt_data(first_name)
    else:
        print("First name cannot be empty.")
        valid_input = False
        
    if last_name:
        traveller_data["last_name_enc"] = encrypt_data(last_name)
    else:
        print("Last name cannot be empty.") 
        valid_input = False

    if birthday:
        valid, msg = validate_iso_date(birthday)
        if not valid:
            print(f"Invalid birthday: {msg}")
            valid_input = False
        else:
            traveller_data["birthday_enc"] = encrypt_data(birthday)
    else:
        print("Birthday cannot be empty.")
        valid_input = False
        
    if gender:
        traveller_data["gender_enc"] = encrypt_data(gender)
    else:
        print("Gender cannot be empty.")
        valid_input = False
        
    if street_name:
        traveller_data["street_name_enc"] = encrypt_data(street_name)
    else:
        print("Street name cannot be empty.")
        valid_input = False
        
    if house_number:
        traveller_data["house_number_enc"] = encrypt_data(house_number)
    else:
        print("House number cannot be empty.")
        valid_input = False
        
    if zipcode:
        valid, msg = validate_zip_code(zipcode)
        if not valid:
            print(f"Invalid zipcode: {msg}") 
            valid_input = False
        else:
            traveller_data["zip_code_enc"] = encrypt_data(zipcode)
    else:
        print("Zipcode cannot be empty.")
        valid_input = False
        
    if city:
        valid, msg = validate_city(city)
        if not valid:
            print(f"Invalid city: {msg}")
            valid_input = False
        else:
            traveller_data["city_enc"] = encrypt_data(city)
    else:
        print("City cannot be empty.")
        valid_input = False
        
    if email:
        traveller_data["email_address_enc"] = encrypt_data(email)
    else:
        print("Email cannot be empty.")
        valid_input = False
        
    if number:
        valid, msg = validate_mobile_phone(number)
        if not valid:
            print(f"Invalid phone number: {msg}")
            valid_input = False
        else:
            traveller_data["mobile_phone_enc"] = encrypt_data(number)
    else:
        print("Phone number cannot be empty.")
        valid_input = False
        
    if license_number:
        valid, msg = validate_driving_license(license_number)
        if not valid:
            print(f"Invalid driving license number: {msg}")
            valid_input = False
        else:
            traveller_data["driving_license_number_enc"] = encrypt_data(license_number)
    else:
        print("Driving license number cannot be empty.")
        valid_input = False
        
    traveller_data["registration_date"] = registration_date

    if valid_input:
        db.create_traveller(**traveller_data)
    else:
        print("Traveller not added due to invalid input.")

def add_scooter():
    db = DatabaseManager("database/data/urban_mobility.db")

    brand = input("Enter a brand: ")
    model = input("Enter a model: ")
    serial_number = input("Enter a serial number: ")
    top_speed = input("Enter a top speed: ")
    battery_capacity = input("Enter a battery capacity: ")
    state_of_charge = input("Enter a state of charge: ")
    target_range = input("Enter a target range: ")
    location = input("Enter a location: ")
    out_of_service_status = input("Enter the out-of-service status: ")
    mileage = input("Enter the mileage: ")
    last_maintenance_date = input("Enter the last maintenance date (yyyy-mm-dd): ")
    in_service_date = datetime.now().strftime("%Y-%m-%d")
    
    scooter_data = {}
    valid_input = True

    if brand:
        scooter_data["brand"] = brand
    else:
        print("Brand cannot be empty.")
        valid_input = False
    if model:
        scooter_data["model"] = model
    else:
        print("Model cannot be empty.")
        valid_input = False

    if serial_number:
        valid, msg = validate_serial_number(serial_number)
        if not valid:
            print(f"Invalid serial number: {msg}") 
            valid_input = False
        else:
            scooter_data["serial_number"] = encrypt_data(serial_number)
    else:
        print("Serial number cannot be empty.")
        valid_input = False

    if top_speed:
        scooter_data["top_speed"] = top_speed
    else:
        print("Top speed cannot be empty.")
        valid_input = False
    if battery_capacity:
        scooter_data["battery_capacity"] = battery_capacity
    else:
        print("Battery capacity cannot be empty.")
        valid_input = False
    if state_of_charge:
        scooter_data["state_of_charge"] = state_of_charge
    else:
        print("State of charge cannot be empty.")
        valid_input = False
    if target_range:
        scooter_data["target_range_soc"] = target_range
    else:
        print("Target range cannot be empty.")
        valid_input = False

    if location:
        try:
            lat_str, lon_str = map(str.strip, location.split(","))
            valid, msg = validate_location(lat_str, lon_str)
            if not valid:
                print(f"Invalid location: {msg}")
                valid_input = False
            else:
                scooter_data["location_enc"] = encrypt_data(location)
        except ValueError:
            print("Location must be in the format 'latitude, longitude'.")
            valid_input = False
    else:
        print("Location cannot be empty.")
        valid_input = False

    if out_of_service_status:
        scooter_data["out_of_service_status"] = out_of_service_status
    else:
        print("Out-of-service status cannot be empty.")
        valid_input = False

    if mileage:
        scooter_data["mileage"] = mileage
    else:
        print("Mileage cannot be empty.")
        valid_input = False

    if last_maintenance_date:
        valid, msg = validate_iso_date(last_maintenance_date)
        if not valid:
            print(f"Invalid last maintenance date: {msg}")
            valid_input = False
        else:
            scooter_data["last_maintenance_date"] = last_maintenance_date
    else:
        print("Last maintenance date cannot be empty.")
        valid_input = False

    scooter_data["in_service_date"] = in_service_date

    if valid_input:
        db.create_scooter(**scooter_data)
    else:
        print("Scooter not added due to invalid input.")

def add_user():
    db = DatabaseManager("database/data/urban_mobility.db")

    errors = []

    username = input("Enter a username: ")
    if not db.is_username_unique(username):
        errors.append("Username already in use.")
    valid, message = validate_username(username)
    if not valid:
        errors.append(f"Username not valid: {message}")

    password = input("Enter a password: ")
    valid, message = validate_password(password)
    if not valid:
        errors.append(f"Password not valid: {message}")
    else:
        password_hash = hash_password(password)

    role = input("Enter a role (e.g., Super Admin, System Admin, Service Engineer): ")
    if role.lower() != "super admin" and role.lower() != "system admin" and role.lower() != "service engineer":
        errors.append("Invalid role.")
    if not role:
        errors.append("Role cannot be empty.")

    first_name = input("Enter a first name: ")
    if not first_name:
        errors.append("First name cannot be empty.")

    last_name = input("Enter a last name: ")
    if not last_name:
        errors.append("Last name cannot be empty.")

    if errors:
        print("Input errors found:")
        for error in errors:
            print(f"- {error}")
        print("User not added due to invalid input.")
    else:
        registration_date = datetime.now().strftime("%Y-%m-%d")

        user_data = {
            "username": encrypt_data(username),
            "password_hash": encrypt_data(password_hash),
            "role": role,
            "first_name": encrypt_data(first_name),
            "last_name": encrypt_data(last_name),
            "registration_date": registration_date
        }

        db.create_user(**user_data)

def add_restore_code():
    db = DatabaseManager("database/data/urban_mobility.db")

    errors = []

    code = input("Enter a restore code: ")
    if not code:
        errors.append("Restore code cannot be empty.")

    sys_admin_id = input("Enter the ID of the system admin: ")
    if not sys_admin_id.isdigit():
        errors.append("System admin ID must be a number.")

    backup_file_name = input("Enter the backup file name: ")
    if not backup_file_name:
        errors.append("Backup file name cannot be empty.")

    if errors:
        print("Input errors found:")
        for error in errors:
            print(f"- {error}")
        print("Restore code not added due to invalid input.")
    else:
        generated_at = datetime.now().strftime("%Y-%m-%d")
        is_used = 0

        restore_code_data = {
            "code": encrypt_data(code),
            "system_admin_id": int(sys_admin_id),
            "backup_file_name": backup_file_name,
            "is_used": is_used,
            "generated_at": generated_at
        }

        db.create_restore_code(**restore_code_data)