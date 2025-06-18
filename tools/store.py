import asyncio
import csv
import os

CSV_File = "registration.csv"

async def store_data(data: dict) -> str:
    name = data.get("name")
    email = data.get("email")
    dob = data.get("dob")

    if not all([name, email, dob]):
        return "Missing fields. Please include name, email, and dob."

    with open(CSV_File, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, dob])

    return f"Stored: {name}, {email}, {dob}"

