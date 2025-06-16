from SysAdminUI import sys_admin_ui
from database_stuff.DBOperations import populate_roles
from database_stuff.DBOperations import clear_database

def main():
    sys_admin_ui()

if __name__ == "__main__":
    # TODO: INPUT VALIDATION & ERROR HANDLING IN add_traveller.py
    # TODO: ERROR HANDLING IN DBOperations.py
    main() 