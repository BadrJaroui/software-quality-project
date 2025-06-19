import os
from datetime import datetime
from database.database import DatabaseManager
from frontend.search import search_traveller_ui
from frontend.create import add_user, add_restore_code, add_traveller
from frontend.delete import delete_restore_code
from frontend.update import update_user
from frontend.sys_admin_ui import sys_admin_ui
from frontend.service_engineer_ui import service_engineer_ui
from logs.logging_file import create_log_file, add_log_entry, view_log_file
from database.backup_db import restore_db_with_code, backup_db

from security.security import load_encryption_key

def main():
    add_user()

if __name__ == "__main__":
    # TODO: LOGGING IN RELEVANT AREAS
    # TODO: SUPER ADMIN PANEL & FUNCTIONS
    # TODO: LOGIN SYSTEM
    # TODO: FIRST 6 BULLET POINTS OF SYS ADMIN
    main()
