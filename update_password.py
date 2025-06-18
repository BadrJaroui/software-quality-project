from security.security import decrypt_data
from security.security import encrypt_data
from security.security import hash_password
from database.database import DatabaseManager
from CurrentLoggedInUser import currentUserID

def update_password(new_pass):
    hashed_pass = hash_password(new_pass)

    query = "UPDATE users SET password_hash = ? WHERE id = ?",
    (hashed_pass, currentUserID)