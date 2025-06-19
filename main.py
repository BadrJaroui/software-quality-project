import os
from datetime import datetime
from database.database import DatabaseManager
from frontend.search import search_traveller_ui
from frontend.create import add_user, add_restore_code, add_traveller
from frontend.delete import delete_restore_code
from frontend.sys_admin_ui import sys_admin_ui
from frontend.service_engineer_ui import service_engineer_ui
from logs.logging_file import create_log_file, add_log_entry, view_log_file
from database.backup_db import restore_db_with_code, backup_db

from security.security import load_encryption_key

def main():
    sys_admin_ui()

if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: LOGGING IN RELEVANT AREAS
    # TODO: TEST SERVICE ENGINEER FUNCTIONS
    # TODO: CHECK IF USERNAME IS UNIQUE
    main()
