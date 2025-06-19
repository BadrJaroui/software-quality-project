import bcrypt # You'll need to install this: pip install bcrypt
from cryptography.fernet import Fernet # You'll need to install this: pip install cryptography
from datetime import datetime
import re
import os


def generate_encryption_key():
    os.makedirs(os.path.dirname("./secrets/encryption_key.key"), exist_ok=True)
    key = Fernet.generate_key()
    with open("./secrets/encryption_key.key", 'wb') as key_file:
        key_file.write(key)

    return key


def load_encryption_key(key_file="./secrets/encryption_key.key"):
    if not os.path.exists(key_file):
        key = generate_encryption_key()
        with open(key_file, "wb") as f:
            f.write(key)
        print("Generated new encryption key.")
    else:
        with open(key_file, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_encryption_key()

def encrypt_data(data):
    if data is None:
        return None
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    if encrypted_data is None:
        return None
    try:
        return fernet.decrypt(encrypted_data.encode()).decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def validate_username(username):
    if not (8 <= len(username) <= 10):
        return False, "Username must be between 8 and 10 characters long."
    if not re.match(r"^[a-zA-Z_]", username):
        return False, "Username must start with a letter or an underscore."
    if not re.match(r"^[a-zA-Z0-9_'.]*$", username):
        return False, "Username can only contain letters, numbers, underscores, apostrophes, and periods."
    return True, ""

def validate_password(password):
    if not (12 <= len(password) <= 30):
        return False, "Password must be between 12 and 30 characters long."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[~!@#$%^&*+=´|V(){}\[\]:;'<>,.?/]", password):
        return False, "Password must contain at least one special character."
    return True, ""

def validate_zip_code(zip_code):
    if not re.match(r"^\d{4}[A-Z]{2}$", zip_code):
        return False, "Zip Code must be in DDDDXX format (e.g., 1234AB)."
    return True, ""

def validate_city(city):
    valid_cities = {
    "Centrum",
    "Kralingen",
    "Delfshaven",
    "Noord",
    "Feijenoord",
    "Overschie",
    "Hillegersberg-Schiebroek",
    "Prins Alexander",
    "Charlois",
    "Hoek van Holland"
    }
    if city not in valid_cities:
        return False, f"City must be one of: {', '.join(valid_cities)}."
    return True, ""

def validate_mobile_phone(phone_number):
    if not re.match(r"^\d{8}$", phone_number):
        return False, "Mobile Phone must be exactly 8 digits (e.g., 12345678)."
    return True, ""

def validate_driving_license(license_number):
    if not re.match(r"^[A-Z]{1,2}\d{7,8}$", license_number):
        return False, "Driving license must be in the format XXDDDDDDD or XDDDDDDDD."
    return True, ""

def validate_serial_number(serial_number):
    if not re.match(r"^[a-zA-Z0-9]{10,17}$", serial_number):
        return False, "Serial number must be 10 to 17 alphanumeric characters."
    return True, ""

def validate_location(latitude, longitude):
    try:
        lat = float(latitude)
        lon = float(longitude)

        if len(str(lat).split('.')[-1]) > 5 or len(str(lon).split('.')[-1]) > 5:
            return False, "Latitude and Longitude must have at most 5 decimal places."

        if not (51.85 < lat < 52.05 and 4.35 < lon < 4.65):
            return False, "Location must be within the Rotterdam region."
    except ValueError:
        return False, "Latitude and Longitude must be valid numbers."
    return True, ""

def validate_iso_date(date_string):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_string):
        return False, "Date must be in ISO 8601 format yyyy-mm-dd."
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return False, "Invalid date value."
    return True, ""

def decrypt_scooter_data(row):
    if not row:
        return None
    decrypted_row = list(row)
    encrypted_indexes = [3, 8]
    for i in encrypted_indexes:
        decrypted_row[i] = decrypt_data(decrypted_row[i])
    return tuple(decrypted_row)

def decrypt_traveller_data(row):
    if not row:
        return None
    decrypted_row = list(row)
    encrypted_indexes = list(range(1, 12))
    for i in encrypted_indexes:
        decrypted_row[i] = decrypt_data(decrypted_row[i])
    return tuple(decrypted_row)

def decrypt_user_data(row):
    if not row:
        return None
    decrypted_row = list(row)
    for i in range(1, 6):
        decrypted_row[i] = decrypt_data(decrypted_row[i])
    return tuple(decrypted_row)