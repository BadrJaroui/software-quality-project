from DBOperations import DeleteAccount
from backup_db import backup_db
from CurrentLoggedInUser import currentUserID

def sys_admin_ui():
    print("1. Backup system")
    print("2. Delete Account")
    
    input_value = input()

    if input_value == "1":
        backup_db()
        # Return to login screen
    
    if input_value == '2':
        # Add a confirmation
        DeleteAccount(currentUserID)
        # Return to login screen
        
