import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="urban_mobility.db", db_dir="./database/data"):
        os.makedirs(db_dir, exist_ok=True)

        self.db_path = os.path.join(db_dir, db_name)

        print(f"Database will be created at: {self.db_path}")

        self._create_tables()

    def _create_tables(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Users table (for Super Admin, System Admin, Service Engineer)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL,
                    first_name TEXT,
                    last_name TEXT,
                    registration_date TEXT
                )
            ''')

            # Travellers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS travellers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name_enc TEXT NOT NULL,
                    last_name_enc TEXT NOT NULL,
                    birthday_enc TEXT,
                    gender_enc TEXT,
                    street_name_enc TEXT,
                    house_number_enc TEXT,
                    zip_code_enc TEXT,
                    city_enc TEXT,
                    email_address_enc TEXT,
                    mobile_phone_enc TEXT,
                    driving_license_number_enc TEXT,
                    registration_date TEXT NOT NULL
                )
            ''')

            # Scooters table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scooters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    brand TEXT NOT NULL,
                    model TEXT NOT NULL,
                    serial_number TEXT UNIQUE NOT NULL,
                    top_speed REAL,
                    battery_capacity REAL,
                    state_of_charge REAL,
                    target_range_soc TEXT,
                    location_enc TEXT,
                    out_of_service_status INTEGER, -- 0 for no, 1 for yes
                    mileage REAL,
                    last_maintenance_date TEXT,
                    in_service_date TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS restore_codes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT UNIQUE NOT NULL,
                    system_admin_id INTEGER NOT NULL,
                    backup_file_name TEXT NOT NULL,
                    is_used INTEGER DEFAULT 0, -- 0 for not used, 1 for used
                    generated_at TEXT NOT NULL,
                    FOREIGN KEY (system_admin_id) REFERENCES users(id)
                )
            ''')

            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during table creation: {e}")
        finally:
            if conn:
                conn.close()

    def execute_query(self, query, params=(), fetch_one=False, fetch_all=False):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            if fetch_one:
                return cursor.fetchone()
            if fetch_all:
                return cursor.fetchall()
            return True
        except sqlite3.Error as e:
            print(f"Database query error: {e}")
            return False
        finally:
            if conn:
                conn.close()
