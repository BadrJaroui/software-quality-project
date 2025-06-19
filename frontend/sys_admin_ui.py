from frontend.create import add_traveller
from frontend.update import update_traveller
from frontend.delete import delete_user
from database.backup_db import backup_db
from database.methods import DatabaseManager
from utils.CurrentLoggedInUser import currentUserID
from utils.utils import clear_terminal
from datetime import datetime

def sys_admin_ui():
    global currentUserID
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
            update_traveller()
            input("Press Enter to return to menu.")

        if input_value == "3":
            clear_terminal()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_db(f"db_backups/backupscooter_{timestamp}.zip")
            input("Press Enter to return to menu.")

        if input_value == '4':
            clear_terminal()
            user_input = input("Are you sure you want to delete your own account? (y/n)")
            if (user_input.lower() == "y"):
                db = DatabaseManager("database/data/urban_mobility.db")
                db.delete_user(currentUserID)
                input("Account has been deleted. Press enter to return to login screen.")
                break
            else:
                continue

        if input_value == "5":
            clear_terminal()
            currentUserID = None
            break
