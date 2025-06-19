from frontend.create import add_traveller, add_scooter
from frontend.update import update_traveller, update_scooter, update_password_ui
from frontend.search import search_traveller_ui, search_scooter_ui
from frontend.delete import delete_traveller, delete_scooter
from database.backup_db import restore_db_with_code, backup_db
from logs.logging_file import view_log_file, check_log_file_exists
from database.methods import DatabaseManager
from utils.CurrentLoggedInUser import currentUserID
from utils.utils import clear_terminal
from datetime import datetime

def sys_admin_ui():
    global currentUserID
    while True:
        clear_terminal()
        print("1. Search traveller")
        print("2. Add a traveller")
        print("3. Update traveller")
        print("4. Delete traveller")
        print("5. Search scooter")
        print("6. Add scooter")
        print("7. Update scooter")
        print("8. Delete scooter")
        print("9. Backup system")
        print("0. Logout")
        print("L. View logs")
        print("R. Restore backup")
        print("Q. Update password")
        print("Z. Delete own account")

        input_value = input()

        if input_value == "1":
            clear_terminal()
            search_traveller_ui()
            input("Press Enter to return to menu.")

        if input_value == "2":
            clear_terminal()
            add_traveller()
            input("Press Enter to return to menu.")

        if input_value == "3":
            clear_terminal()
            update_traveller()
            input("Press Enter to return to menu.")

        if input_value == "4":
            clear_terminal()
            delete_traveller()
            input("Press Enter to return to menu.")

        if input_value == "5":
            clear_terminal()
            search_scooter_ui()
            input("Press Enter to return to menu.")

        if input_value == "6":
            clear_terminal()
            add_scooter()
            input("Press Enter to return to menu.")

        if input_value == "7":
            clear_terminal()
            update_scooter()
            input("Press Enter to return to menu.")

        if input_value == "8":
            clear_terminal()
            delete_scooter()
            input("Press Enter to return to menu.")

        if input_value == "9":
            clear_terminal()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_db(f"db_backups/backupscooter_{timestamp}.zip")
            input("Press Enter to return to menu.")

        if input_value == "0":
            clear_terminal()
            currentUserID = None
            break

        if input_value.lower() == "l":
            clear_terminal()
            check_log_file_exists()
            view_log_file("logs/activity_log.csv")
            input("Press Enter to return to menu.")

        if input_value.lower() == "q":
            clear_terminal()
            update_password_ui()
            input("Press Enter to return to menu.")

        if input_value.lower() == "r":
            clear_terminal()
            restore_db_with_code()
            input("Press Enter to return to menu.")

        if input_value.lower() == 'z':
            clear_terminal()
            user_input = input("Are you sure you want to delete your own account? (y/n)")
            if (user_input.lower() == "y"):
                db = DatabaseManager("database/data/urban_mobility.db")
                db.delete_user(currentUserID)
                input("Account has been deleted. Press enter to return to login screen.")
                break
            else:
                continue

