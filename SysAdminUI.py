from DBOperations import DeleteAccount
from CurrentLoggedInUser import currentUserID

def sys_admin_ui():
    print("1. Delete Account")
    
    input_value = input()
    
    if input_value == '1':
        # Add a confirmation
        DeleteAccount(currentUserID)
        # Return to login screen
        
