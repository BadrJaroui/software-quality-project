import sqlite3

def DeleteAccount(id):
    conn = sqlite3.connect("scooter.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM roles WHERE id = ?", (id,))
        conn.commit()
    except Exception as ex:
        print(f"Error deleting account: {ex}")
    finally:
        conn.close()