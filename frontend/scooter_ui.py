from database.methods import DatabaseManager

def search_scooter_ui():
    while True:
        print("Search on:\n1. ID\n2. serial number")
        user_input = input()
        scooter = None

        if user_input == "1":
            print("Type an ID:")
            id = input()
            scooter = DatabaseManager.search_scooter(id, None)
        elif user_input == "2":
            print("Type a serial number:")
            serial = input()
            scooter = DatabaseManager.search_scooter(None, serial)

        if not scooter == None:
            print(scooter)
            break
        else:
            print("Scooter does not exist.")
            break

def update_scooter():
    field_choices = []
    field_updates = {}

    field_options = {
        "1": "state_of_charge",
        "2": "target_range_soc",
        "3": "location_enc",
        "4": "out_of_service_status",
        "5": "mileage",
        "6": "last_maintenance_date"
    }

    id_input = input("Enter scooter ID: ")

    while True:
        print("1 State of charge\n" \
        "2. Target range\n" \
        "3. Location\n" \
        "4. Out-of-service status\n" \
        "5. Mileage\n" \
        "6. Last maintenance date\n")
        print("Select fields to update, then type 'done'")
        user_input = input()

        if user_input == "done":
            break
        elif user_input in field_options:
            field = field_options[user_input]
            if field not in field_choices:
                field_choices.append(field)
            else:
                print("Field already selected.")

    

    for field in field_choices:
        new_field = input(f"Enter new {field}: ")
        field_updates[field] = new_field

    DatabaseManager.update_scooter(id_input, field_updates)