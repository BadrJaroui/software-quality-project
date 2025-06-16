from add_traveller import add_traveller
from DBOperations import DeleteAccount
from backup_db import backup_db
from CurrentLoggedInUser import currentUserID
from utils.clear_terminal import clear_terminal

def sys_admin_ui():
    while True:
        clear_terminal()
        print("1. Add a traveller")
        print("2. Backup system")
        print("3. Delete own account")
        print("4. Logout")
        
        input_value = input()

        if input_value == "1":
            clear_terminal()
            add_traveller()
            input("Press Enter to return to menu.")

        if input_value == "2":
            clear_terminal()
            backup_db()
            input("Press Enter to return to menu.")
        
        if input_value == '3':
            # Add a confirmation
            clear_terminal()
            DeleteAccount(currentUserID)
            input("Press Enter to return to menu.")

        if input_value == "4":
            clear_terminal()
            currentUserID = None
            break