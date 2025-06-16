from add_traveller import add_traveller
from update_traveller import update_traveller_ui
from database_stuff.DBOperations import DeleteAccount
from database_stuff.backup_db import backup_db
from CurrentLoggedInUser import currentUserID
from utils.clear_terminal import clear_terminal
from datetime import datetime

def sys_admin_ui():
    while True:
        clear_terminal()
        print("1. Add a traveller")
        print("2. Update traveller data")
        print("3. Backup system")
        print("4. Delete own account")
        print("5. Logout")
        
        input_value = input()

        if input_value == "1":
            clear_terminal()
            add_traveller()
            input("Press Enter to return to menu.")
            
        if input_value == "2":
            clear_terminal()
            update_traveller_ui()
            input("Press Enter to return to menu.")

        if input_value == "3":
            clear_terminal()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_db(f"db_backups/backupscooter_{timestamp}.zip")
            input("Press Enter to return to menu.")
        
        if input_value == '4':
            # Add a confirmation
            clear_terminal()
            DeleteAccount(currentUserID)
            input("Press Enter to return to menu.")

        if input_value == "5":
            clear_terminal()
            currentUserID = None
            break