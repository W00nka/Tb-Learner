import sqlite3
import sys

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
import read_database

conn.commit()

conn.close()