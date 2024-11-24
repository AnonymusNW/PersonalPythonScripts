#!/usr/bin/env python3
import sqlite3
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('count', type = float )
parser.add_argument('protein', type = float )
parser.add_argument('--food', default = "Air", type = str)
args = parser.parse_args()
kalorienDB = sqlite3.connect("Kalorien.db")

cursor = kalorienDB.cursor()
data = {"Count": args.count, "Protein": args.protein, "Food": args.food}
cursor.execute("INSERT INTO Kalorien(count, protein, date, food) VALUES (:Count, :Protein, current_date, :Food )", data)
kalorienDB.commit()
cursor.execute("SELECT SUM(count) FROM Kalorien WHERE date=current_date")
print(cursor.fetchall())
cursor.execute("SELECT SUM(protein) FROM Kalorien WHERE date=current_date")
print(cursor.fetchall())

