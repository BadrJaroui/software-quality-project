from security.security import encrypt_data, decrypt_data
import csv
import os

def create_log_file():
    os.makedirs("logs", exist_ok=True)
    path = "logs/activity_log.csv"

    with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Date", "Time", "Username", "Description", "Suspicious"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    print("Log file does not exist. New log file has been created.")

def check_log_file_exists():
    path = "logs/activity_log.csv"
    if not os.path.exists(path):
        create_log_file()

def add_log_entry(log_entry, path):
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "Time", "Username", "Description", "Suspicious"])
        encrypted_log = {
            "Date": encrypt_data(log_entry["Date"]),
            "Time": encrypt_data(log_entry["Time"]),
            "Username": encrypt_data(log_entry["Username"]),
            "Description": encrypt_data(log_entry["Description"]),
            "Suspicious": encrypt_data(log_entry["Suspicious"]),
        }
        writer.writerow(encrypted_log)

    print("Successfully written to log.")


def view_log_file(path):
    if not os.path.exists(path):
        print("Log file not found.")
        return

    with open(path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("Date:", decrypt_data(row["Date"]))
            print("Time:", decrypt_data(row["Time"]))
            print("Username:", decrypt_data(row["Username"]))
            print("Description:", decrypt_data(row["Description"]))
            print("Suspicious:", decrypt_data(row["Suspicious"]))
            print("-" * 40)