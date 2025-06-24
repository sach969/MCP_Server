import asyncio
import csv
import os

CSV_FILE = "registration.csv"

async def store_data(name: str, email: str, dob: str) -> str:
    if not all([name, email, dob]):
        return "Missing fields. Please include name, email, and dob."

    # Ensure CSV file exists with header
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Email", "DOB"])
        writer.writerow([name, email, dob])

    return f"Stored: {name}, {email}, {dob}"
