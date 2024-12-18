#!/usr/bin/env python3
from datetime import datetime
today = datetime.today()
dates = []
names = []
with open("Events.txt", "r") as file:
    for line in file:
        dates.append(datetime.strptime(line.split(':')[0], '%Y-%m-%d'))
        names.append(line.split(':')[1].strip())

def findNextDateIndex():
    index = 0
    while today > dates[index]:
        index += 1
        if index > len(dates) - 1:
            print("No Events left for this year")
            return -1
    return index 

index = findNextDateIndex()
if index >= 0:
    print(f"The next Event is {names[index]} in {dates[index] - today} days")

