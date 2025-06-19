import os
import sqlite3
import zipfile
import shutil
from utils.CurrentLoggedInUser import currentUserID
from database.methods import DatabaseManager

def backup_db(zip_path, source_db="database/data/urban_mobility.db"):
    folder = os.path.dirname(zip_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    temp_backup_path = os.path.join(folder, "temp_backup.db")

    source = sqlite3.connect(source_db)
    destination = sqlite3.connect(temp_backup_path)
    with destination:
        source.backup(destination)
    source.close()
    destination.close()

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(temp_backup_path, arcname=os.path.basename(source_db))

    os.remove(temp_backup_path)

    print("Backup created.")
    print("Backup path (absolute):", os.path.abspath(zip_path))

def restore_db(zip_path, restore_to="database/data/urban_mobility.db"):
    folder = os.path.dirname(restore_to)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if os.path.exists(restore_to):
        os.remove(restore_to)

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(folder)

    print("Database restored.")
    print("Restored from:", os.path.abspath(zip_path))

def restore_db_with_code():
    db = DatabaseManager("database/data/urban_mobility.db")
    
    restore_code = input("Enter a restore code: ")
    if (db.get_restore_code(restore_code, currentUserID)):
        restore_db("db_backups/" + db.get_backup_file_name(restore_code, currentUserID))
    else:
        print("The code you have entered does not match any records. Notify an administrator.")