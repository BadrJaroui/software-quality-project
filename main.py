import os
from frontend.SysAdminUI import sys_admin_ui
from logs.logging_file import create_log_file
from logs.logging_file import add_log_entry

from security.security import load_encryption_key

def main():
    log_entry = {
        "Date": "2025-06-16",
        "Time": "13:45:22",
        "Username": "jdoe",
        "Description": "Accessed secure area of the system",
        "Suspicious": "False"
    }
    path = "logs/activity_log.csv"
    key = load_encryption_key()

    add_log_entry(log_entry, path, key)


if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: ERROR HANDLING IN DBOperations.py
    # TODO: LOGGING IN RELEVANT AREAS
    main()
