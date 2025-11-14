import sqlite3


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


adder()
#import read_database

