import sqlite3

def backup_db(backup_db, source_db = "database/scooter.db"):
    source = sqlite3.connect(source_db)
    destination = sqlite3.connect(backup_db)

    with destination:
        source.backup(destination)
        
    source.close()
    destination.close()