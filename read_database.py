import sqlite3

conn = sqlite3.connect("vocabulary.db")
cur = conn.cursor()

cur.execute("SELECT * FROM vocabs")
for row in cur.fetchall():
    print(row)

conn.close()