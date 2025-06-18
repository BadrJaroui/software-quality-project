import os
from database.database import DatabaseManager
from frontend.create import add_user
from frontend.update import update_user
from frontend.delete import delete_user
from frontend.SysAdminUI import sys_admin_ui
from frontend.service_engineer_ui import service_engineer_ui
from logs.logging_file import create_log_file
from logs.logging_file import add_log_entry

from security.security import load_encryption_key

def main():
    pass

if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: LOGGING IN RELEVANT AREAS
    # TODO: TEST SERVICE ENGINEER FUNCTIONS
    # TODO: CHECK IF USERNAME IS UNIQUE
    main()
