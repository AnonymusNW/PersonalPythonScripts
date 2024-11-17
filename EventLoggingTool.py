#!/usr/bin/env python3
import datetime
import BSort

def appendDate():
    month = int(input("Enter a month:\n"))
    day = int(input("Enter a day:\n"))
    actualDate = datetime.date(datetime.datetime.now().year, month, day)
    name = str(input("Enter the name of the event: "))
    eventsList= open("Events.txt", "r+")
    eventsList.write(f"{actualDate}: {name}\n")

def sortFile():
    events = []
    with open("Events.txt", "r+") as eventsList:
        for line in eventsList:
            events.append((datetime.datetime.strptime(line.split(':')[0], '%Y-%m-%d'), line.split(':')[1].strip()))
        events = BSort.bubble_sort(events)
        for event in events:
            eventsList.write(f"{event[0].date}: {event[1]}\n")

count = int(input("How many entries?:\n"))
for i in range(count):
    appendDate()
sortFile()


