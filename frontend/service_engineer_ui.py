from utils.utils import clear_terminal
from database.methods import DatabaseManager
from frontend.search import search_scooter_ui
from frontend.update import update_scooter
from frontend.update import update_password_ui

def service_engineer_ui():
    while True:
        clear_terminal()
        print("1. Search scooter information")
        print("2. Update scooter attributes")
        print("3. Update password")
        print("4. Logout")
        
        input_value = input()

        if input_value == "1":
            clear_terminal()
            search_scooter_ui()
            input("Press Enter to return to menu.")
            
        if input_value == "2":
            clear_terminal()
            update_scooter()
            input("Press Enter to return to menu.")

        if input_value == "3":
            clear_terminal()
            update_password_ui()
            input("Press Enter to return to menu.")

        if input_value == "4":
            clear_terminal()
            currentUserID = None
            break