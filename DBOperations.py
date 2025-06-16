import sqlite3

def DeleteAccount(id, path = "database/scooter.db"):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM roles WHERE id = ?", (id,))
        conn.commit()
    except Exception as ex:
        print(f"Error deleting account: {ex}")
    finally:
        conn.close()

def create_traveller(traveller_data, path = "database/scooter.db"):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO travellers (FirstName, LastName, Birthday, Gender, ZipCode, City, EmailAddress, MobilePhone, LicenseNumber)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', traveller_data)
    
    conn.commit()
    conn.close()


def populate_roles(path = "database/scooter.db"):
    roles = [(1, "super_admin"), (2, "system_admin"), (3, "service_engineer")]

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    for role_id, role_name in roles:
        cursor.execute('''
            INSERT INTO roles (id, role)
            VALUES (?, ?)
        ''', (role_id, role_name))

    conn.commit()
    conn.close()

def clear_database(path = "database/scooter.db"):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    tables = ["roles", "scooters", "travellers"]

    for table in tables:
        cursor.execute(f"DELETE FROM {table}")
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table}"')

    conn.commit()
    conn.close()