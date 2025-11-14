import sqlite3
import random
import os
import time
import sys
import importlib

counter = [[None],[None],[None],[None],[None],[None]]
os.system('clear')
print("Wilkommen in Tb-Learner \n \n \n \nMade by W00nka")
time.sleep(2)

# Home 
def home():
    os.system('clear')
    print("Willkommen in deinem Home-Dashboard")
    print("Was möchtest du tun? \n [0] Kapitel wiederholen \n [1] Gamemodes \n [2] Wörterbuch \n [3] Fehler wiederholen \n [4] Statistiken \n [5] Datenbank verändern \n [6] Exit")

# Exit
def exit_function():
    sys.exit()

# Redirect
def director(choice):
    if choice == 0:
        from Modes import chapter_learner
        if counter[choice][0] is not None:
            importlib.reload(chapter_learner)
    if choice == 1: 
        from Modes import gamemodes
        if counter[choice][0] is not None:
            importlib.reload(gamemodes)
    if choice == 2:
        from Modes import dictonary
        if counter[choice][0] is not None:
            importlib.reload(dictonary)
    if choice == 3:
        from Modes import error_correct
        if counter[choice][0] is not None:
            importlib.reload(error_correct)
    if choice == 4:
        from Modes import stats
        if counter[choice][0] is not None:
            importlib.reload(stats)
    if choice == 5:
        from Modes import database
        if counter[choice][0] is not None:
            importlib.reload(database)
    if choice == 6:
        sys.exit()
 
# Runtime
home()
choice = int(input("\n \n \nWähle bitte eine Zahl \"0-6\" : "))
director(choice)
while True:
    counter[choice].insert(0, choice)
    home() 
    choice = int(input("\n \n \nWähle bitte eine Zahl \"0-6\" : "))
    director(choice)

