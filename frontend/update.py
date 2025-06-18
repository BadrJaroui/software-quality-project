from database.methods import DatabaseManager
def update_traveller():

    traveller_id = input("Enter the ID of the traveller to update: ")

    print("Enter new values (leave blank to skip updating a field):")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birthday = input("Birthday: ")
    gender = input("Gender: ")
    zipcode = input("Zipcode: ")
    city = input("City: ")
    email = input("Email: ")
    number = input("Phone number: ")
    license_number = input("License number: ")

    updates = {}
    if first_name: updates["first_name"] = first_name
    if last_name: updates["last_name"] = last_name
    if birthday: updates["birthday"] = birthday
    if gender: updates["gender"] = gender
    if zipcode: updates["zipcode"] = zipcode
    if city: updates["city"] = city
    if email: updates["email"] = email
    if number: updates["number"] = number
    if license_number: updates["license_number"] = license_number

    if updates:
        DatabaseManager.update_traveller(int(traveller_id), **updates)
        print("Traveller updated successfully!")
    else:
        print("No updates provided.")
