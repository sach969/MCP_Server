import asyncio
import csv
import os

CSV_FILE = "registration.csv"

async def fetch_data():
    if not os.path.exists(CSV_FILE):
        return "No data found"
    
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        if not rows:
            return "CSV is empty"
        return "\n".join([", ".join(row) for row in rows])