from database.methods import DatabaseManager

def add_traveller():
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    birthday = input("Enter a birthday: ")
    gender = input("Enter a gender: ")
    zipcode = input("Enter a zipcode: ")
    city = input("Enter a city: ")
    email = input("Enter an email address: ")
    number = input("Enter a phone number: ")
    license_number = input("Enter a license number: ")

    traveller_data = (
        first_name, last_name, birthday, gender,
        zipcode, city, email, number, license_number
    )
    DatabaseManager.create_traveller(traveller_data)
    print("Traveller added successfully!")
