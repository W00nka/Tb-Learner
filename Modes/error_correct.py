import time
import os
import sqlite3

def reader():
    os.system('clear')
    print("Hier kannst du deine Fehler sehen:")
    conn = sqlite3.connect("error.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM error")
    for row in cur.fetchall():
        print(row)

    conn.close()
    input("Press \"Enter\" to Continue...!")

def corrector():
    print("Here I shall correct")

def home():
    os.system('clear')
    print("Willkommen in deiner eigenen Fehler Datenbank! \nHier werden all deine Fehler gespeichert. \nWas möchtest du tun? \n [0] Fehler ansehen? \n [1] Fehler korrigieren")
    choice = int(input("\n \nWähle eine Zahl zwischen 0-1 : "))
    decider(choice)

def decider(choice):
    if choice == 0:
        reader()
    else:
        corrector()

home()

