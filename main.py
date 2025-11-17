import sqlite3
import random
import os
import time
import sys
import importlib

## Homescreen + Variables
counter = [[None],[None],[None],[None],[None],[None]]
gamemodes = [[None], [None]]
os.system('clear')
print("Willkommen in Tb-Learner")
time.sleep(1)

## Home 
def home():
    os.system('clear')
    print("Willkommen in deinem Home-Dashboard")
    print("Was möchtest du tun? \n [0] Vokabeltrainer \n [1] Gamemodes \n [2] Wörterbuch \n [3] Fehler wiederholen \n [4] Statistiken \n [5] Datenbank verändern \n [6] Exit")

## Exit
def exit_function():
    sys.exit()

## Redirect
def director(choice):
    if choice == 0:
        from Modes import vocabulary_learner
        if counter[choice][0] is not None:
            importlib.reload(vocabulary_learner)
    if choice == 1: 
        os.system('clear')
        print("Herzlich Willkommen im Gaming Hub! \nHier kannst du deine gelernten Vokabeln auf die Probe stellen. \nWas möchtest du tun? \n [0] Endless mode \n [1] RANDOM \n \n \n")
        global gamemode_choice
        gamemode_choice = int(input("Wähle bitte eine Zahl \"0-1\" : "))

        if gamemode_choice == 0:
            from Modes.Gamemodes import endless_mode
            if gamemodes[gamemode_choice][0] is not None:
                importlib.reload(endless_mode)
        else:
            from Modes.Gamemodes import RANDOM
            if gamemodes[gamemode_choice][0] is not None:
                importlib.reload(RANDOM)
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
 
## Runtime
home()
choice = int(input("\n \n \nWähle bitte eine Zahl \"0-6\" : "))
director(choice)
while True:
    counter[choice].insert(0, choice)
    home() 
    choice = int(input("\n \n \nWähle bitte eine Zahl \"0-6\" : "))
    director(choice)
    if choice == 1:
        gamemodes[gamemode_choice].insert(0, gamemode_choice)