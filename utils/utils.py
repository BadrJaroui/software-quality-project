import os
from database.methods import DatabaseManager
from security.security import hash_password

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# FIX THIS
def update_password(id, new_pass):
    hashed_pass = hash_password(new_pass)

    update_dict = {"password_hash" : hashed_pass}
    DatabaseManager.update_user(id, update_dict)