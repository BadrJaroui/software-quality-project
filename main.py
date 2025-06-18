import os
from database.database import DatabaseManager
from frontend.search import search_traveller_ui
from frontend.create import add_scooter
from frontend.SysAdminUI import sys_admin_ui
from frontend.service_engineer_ui import service_engineer_ui
from logs.logging_file import create_log_file
from logs.logging_file import add_log_entry

from security.security import load_encryption_key

def main():
    service_engineer_ui()

if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: LOGGING IN RELEVANT AREAS
    # TODO: TEST SERVICE ENGINEER FUNCTIONS
    # TODO: CHECK IF USERNAME IS UNIQUE
    main()
