from DBOperations import create_traveller

def add_traveller():
    print("Enter a first name: ")
    first_name = input()
    print("Enter a last name: ")
    last_name = input()
    print("Enter a birthday: ")
    birthday = input()
    print("Enter a gender: ")
    gender = input()
    print("Enter a zipcode: ")
    zipcode = input()
    print("Enter a city: ")
    city = input()
    print("Enter an email address: ")
    email = input()
    print("Enter a phone number: ")
    number = input()
    print("Enter a license number: ")
    license_number = input()

    create_traveller((first_name, last_name, birthday, gender, zipcode, city, email, number, license_number))