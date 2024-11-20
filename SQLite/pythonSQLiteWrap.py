#!/usr/bin/env python3

import sqlite3

kalorienDB = sqlite3.connect("Kalorien.db")

cursor = kalorienDB.cursor()
datum = "Datum"
kalorien = 200
cursor.execute(f"UPDATE Kalorien SET Kalorien ={kalorien} WHERE Datum=current_date")
cursor.execute("SELECT Kalorien FROM Kalorien WHERE Datum=current_date")
print(cursor.fetchall())
