import sqlite3
import sys
import os
import time
import importlib

def reader():
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM vocabs")
    for row in cur.fetchall():
        print(row)

    conn.close()

def deleter():
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()

    value = input("Delete= 1:Chapter; 2:Russian; 3:German : ")

    if value == "1":
        search_chapter = input("Enter Chapter to delete: ")
        cur.execute("DELETE FROM vocabs WHERE chapter = ?", (search_chapter,))
    elif value == "2":
        search_russian = input("Enter Russian-Word to delete: ")
        cur.execute("DELETE FROM vocabs WHERE russian = ?", (search_russian,))
    elif value == "3":
        search_german = input("Enter German-Word to delete: ")
        cur.execute("DELETE FROM vocabs WHERE german = ?", (search_german,))
    else:
        print("Invalid Input")
        sys.exit()

    print("Value: " + value + " has been successfully deleted")
    reader()

    conn.commit()

    conn.close()

def add_to_database(chapter, russian, german):
    conn = sqlite3.connect("vocabulary.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS vocabs (
        chapter INTEGER,
        russian TEXT,
        german TEXT,
        additional Text
    )
    """)

    daten = [ (chapter, russian, german) ]

    cur.executemany("INSERT INTO vocabs (chapter, russian, german) VALUES (?, ?, ?)", daten)

    conn.commit()

    print("Your  word: \"" + russian + "\" was successfully added to the Database")

    conn.close()

def adder():
    chapter = input("Enter your Chapter: ")
    russian = input("Enter your russian word: ")
    german = input("Enter your german word: ")
    
    add_to_database(chapter, russian, german)

def data_base_manager():
    os.system('clear')
    print("Willkommen im Database-Manager! \nWas möchtest du tun? \n [0] Deine Datenbank auslesen? \n [1] Deine Datenbank mit einem Filter auslesen? \n [2] Deiner Datenbank einen neuen Eintrag geben? \n [3] Inhalt in deiner Datenbank löschen?\n \n \n")
    data = int(input("Wähle eine Zahl zwischen 0-3 : "))
    decider(data)

def decider(data):
    if data == 0:
        os.system('clear')
        reader()
        input("Press \"Enter\" to continue")
    if data == 1:
        print("Work in progress")
        time.sleep(3)
    if data == 2:
        adder()
        input("Press \"Enter\" to continue")
    if data == 3:
        deleter()
        input("Press \"Enter\" to continue")

data_base_manager()
