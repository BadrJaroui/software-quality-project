from database.methods import DatabaseManager
from security.security import hash_password, validate_password, validate_username
from datetime import datetime

def add_traveller():
    db = DatabaseManager("database/data/urban_mobility.db")

    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    birthday = input("Enter a birthday: ")
    gender = input("Enter a gender: ")
    street_name = input("Enter a street name: ")
    house_number_enc = input("Enter a house number: ")
    zipcode = input("Enter a zipcode: ")
    city = input("Enter a city: ")
    email = input("Enter an email address: ")
    number = input("Enter a phone number: ")
    license_number = input("Enter a license number: ")
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    traveller_data = {
        "first_name_enc": first_name,
        "last_name_enc": last_name,
        "birthday_enc": birthday,
        "gender_enc": gender,
        "street_name_enc" : street_name,
        "house_number_enc" : house_number_enc,
        "zip_code_enc": zipcode,
        "city_enc": city,
        "email_address_enc": email,
        "mobile_phone_enc": number,
        "driving_license_number_enc": license_number,
        "registration_date" : registration_date
    }
    db.create_traveller(**traveller_data)
    print("Traveller added successfully!")

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
    last_maintenance_date = input("Enter the last maintenance date: ")
    in_service_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    scooter_data = {
        "brand": brand,
        "model": model,
        "serial_number": serial_number,
        "top_speed": top_speed,
        "battery_capacity" : battery_capacity,
        "state_of_charge" : state_of_charge,
        "target_range_soc": target_range,
        "location_enc": location,
        "out_of_service_status": out_of_service_status,
        "mileage": mileage,
        "last_maintenance_date": last_maintenance_date,
        "in_service_date" : in_service_date
    }

    db.create_scooter(**scooter_data)
    print("Scooter added successfully!")

def add_user():
    db = DatabaseManager("database/data/urban_mobility.db")

    username = input("Enter a username: ")
    valid, message = validate_username(username)
    if not valid:
        print(f"Username not valid: {message}")
        return

    password = input("Enter a password: ")
    valid, message = validate_password(password)
    if not valid:
        print(f"Password not valid: {message}")
        return
    else:
        password_hash = hash_password(password)

    role = input("Enter a role (e.g., Super Admin, System Admin, Service Engineer): ")
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_data = {
        "username": username,
        "password_hash": password_hash,
        "role": role,
        "first_name": first_name,
        "last_name": last_name,
        "registration_date": registration_date
    }
    
    db.create_user(**user_data)
    print("User added successfully!")

def add_restore_code():
    db = DatabaseManager("database/data/urban_mobility.db")

    code = input("Enter a restore code: ")
    sys_admin_id = input("Enter the ID of the system admin: ")
    backup_file_name = input("Enter the backup file name: ")
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_used = 0  # default to not used

    restore_code_data = {
        "code": code,
        "system_admin_id": sys_admin_id,
        "backup_file_name": backup_file_name,
        "is_used": is_used,
        "generated_at": generated_at
    }

    db.create_restore_code(**restore_code_data)
    print("Restore code added successfully!")