import os
from SysAdminUI import sys_admin_ui
from logging_file import create_log_file
from logging_file import add_log_entry
from utils.encryption import load_public_key
from database_stuff.DBOperations import populate_roles
from database_stuff.DBOperations import clear_database

def main():
    log_entry = {
        "Date": "2025-06-16",
        "Time": "13:45:22",
        "Username": "jdoe",
        "Description": "Accessed secure area of the system",
        "Suspicious": "False"
    }
    path = "logs/activity_log.csv"
    key = load_public_key(secrets_dir=os.path.join("utils", "secrets"))

    add_log_entry(log_entry, path, key)

if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: ERROR HANDLING IN DBOperations.py
    # TODO: LOGGING IN RELEVANT AREAS
    main()