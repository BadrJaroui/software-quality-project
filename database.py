import sqlite3
import os

def create_db(db_folder="database", db_filename="scooter.db"):
    db_path = os.path.join(db_folder, db_filename)

    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
        print(f"Created database folder: {db_folder}")



# Example usage:
if __name__ == "__main__":
    create_db()
