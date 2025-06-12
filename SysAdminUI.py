from DeleteOwnAccount import DeleteOwnAccount

def sys_admin_ui():
    print("1. Delete Account")
    
    input_value = input()
    
    if input_value == '1':
        DeleteOwnAccount()
