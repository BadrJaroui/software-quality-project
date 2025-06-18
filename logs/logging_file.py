from utils.encryption import encrypt_message
import csv
import os

def create_log_file():
    os.makedirs("logs", exist_ok=True)
    path = "logs/activity_log.csv"

    with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Date", "Time", "Username", "Description", "Suspicious"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    print("Log file created.")

def add_log_entry(log_entry, path, key):
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Date", "Time", "Username", "Description", "Suspicious"])
        encrypted_log = {
            "Date": encrypt_message(key, log_entry["Date"]),
            "Time": encrypt_message(key, log_entry["Time"]),
            "Username": encrypt_message(key, log_entry["Username"]),
            "Description": encrypt_message(key, log_entry["Description"]),
            "Suspicious": encrypt_message(key, log_entry["Suspicious"]),
        }
        writer.writerow(encrypted_log)

    print("Successfully written to log.")
