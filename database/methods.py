import sqlite3
from security.security import decrypt_data

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

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

    # -------- SCOOTERS --------
    def create_scooter(self, **fields):
        keys = ', '.join(fields.keys())
        placeholders = ', '.join(['?'] * len(fields))
        query = f"INSERT INTO scooters ({keys}) VALUES ({placeholders})"
        return self.execute_query(query, tuple(fields.values()))

    def update_scooter(self, scooter_id, **updates):
        set_clause = ', '.join([f"{k} = ?" for k in updates])
        query = f"UPDATE scooters SET {set_clause} WHERE id = ?"
        return self.execute_query(query, tuple(updates.values()) + (scooter_id,))

    def delete_scooter(self, scooter_id):
        return self.execute_query("DELETE FROM scooters WHERE id = ?", (scooter_id,))

    def search_scooter(self, id=None, serial_number=None):
        if id is not None:
            query = "SELECT * FROM scooters WHERE id = ?"
            return self.execute_query(query, (id,), fetch_one=True)
        elif serial_number is not None:
            query = "SELECT * FROM scooters WHERE serial_number = ?"
            return self.execute_query(query, (serial_number,), fetch_one=True)
        else:
            return None

    # -------- TRAVELLERS --------
    def create_traveller(self, **fields):
        keys = ', '.join(fields.keys())
        placeholders = ', '.join(['?'] * len(fields))
        query = f"INSERT INTO travellers ({keys}) VALUES ({placeholders})"
        return self.execute_query(query, tuple(fields.values()))

    def update_traveller(self, traveller_id, **updates):
        set_clause = ', '.join([f"{k} = ?" for k in updates])
        query = f"UPDATE travellers SET {set_clause} WHERE id = ?"
        return self.execute_query(query, tuple(updates.values()) + (traveller_id,))

    def delete_traveller(self, traveller_id):
        return self.execute_query("DELETE FROM travellers WHERE id = ?", (traveller_id,))

    def search_traveller(self, id=None, first_name=None, last_name=None, email_address=None):
        if id is not None:
            query = "SELECT * FROM travellers WHERE id = ?"
            return self.execute_query(query, (id,), fetch_one=True)
        elif first_name is not None:
            query = "SELECT * FROM travellers WHERE first_name_enc = ?"
            return self.execute_query(query, (first_name,), fetch_one=True)
        elif last_name is not None:
            query = "SELECT * FROM travellers WHERE last_name_enc = ?"
            return self.execute_query(query, (last_name,), fetch_one=True)
        elif email_address is not None:
            query = "SELECT * FROM travellers WHERE email_address_enc = ?"
            return self.execute_query(query, (email_address,), fetch_one=True)
        else:
            return None

    # -------- USERS --------
    def create_user(self, **fields):
        keys = ', '.join(fields.keys())
        placeholders = ', '.join(['?'] * len(fields))
        query = f"INSERT INTO users ({keys}) VALUES ({placeholders})"
        return self.execute_query(query, tuple(fields.values()))

    def update_user(self, user_id, **updates):
        set_clause = ', '.join([f"{k} = ?" for k in updates])
        query = f"UPDATE users SET {set_clause} WHERE id = ?"
        return self.execute_query(query, tuple(updates.values()) + (user_id,))

    def delete_user(self, user_id):
        return self.execute_query("DELETE FROM users WHERE id = ?", (user_id,))

    def search_user(self, **criteria):
        where_clause = ' AND '.join([f"{k} = ?" for k in criteria])
        query = f"SELECT * FROM users WHERE {where_clause}" if criteria else "SELECT * FROM users"
        return self.execute_query(query, tuple(criteria.values()), fetch_all=True)
    
    def is_username_unique(self, username):
        query = "SELECT username FROM users"
        encrypted_usernames = self.execute_query(query, fetch_all=True)
        
        for (encrypted_username,) in encrypted_usernames:
            decrypted_username = decrypt_data(encrypted_username)
            if decrypted_username == username:
                return False
        return True

    # -------- RESTORE CODES --------
    def create_restore_code(self, **fields):
        keys = ', '.join(fields.keys())
        placeholders = ', '.join(['?'] * len(fields))
        query = f"INSERT INTO restore_codes ({keys}) VALUES ({placeholders})"
        return self.execute_query(query, tuple(fields.values()))
    
    def delete_restore_code(self, code_id):
        return self.execute_query("DELETE FROM restore_codes WHERE id = ?", (code_id,))
    
    def get_restore_code(self, code, sys_admin_id):
        query = """
            SELECT id, backup_file_name, is_used
            FROM restore_codes
            WHERE code = ? AND system_admin_id = ?
        """
        return self.execute_query(query, (code, sys_admin_id), fetch_one=True)
    
    def get_backup_file_name(self, code, sys_admin_id):
        query = """
            SELECT backup_file_name
            FROM restore_codes
            WHERE code = ? AND system_admin_id = ?
        """
        result = self.execute_query(query, (code, sys_admin_id), fetch_one=True)
        return result[0] if result else None
