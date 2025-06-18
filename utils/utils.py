import os
from database.methods import DatabaseManager
from security.security import hash_password

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_password(id, new_pass):
    db = DatabaseManager("database/data/urban_mobility.db")

    hashed_pass = hash_password(new_pass)
    update_dict = {"password_hash" : hashed_pass}
    db.update_user(id, **update_dict)

def get_role_by_id(id):
    db = DatabaseManager("database/data/urban_mobility.db")

    user = db.search_user(id=id)
    user_role = user[0][3]

    return user_role