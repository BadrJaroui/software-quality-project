import os
import sqlite3
import zipfile

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