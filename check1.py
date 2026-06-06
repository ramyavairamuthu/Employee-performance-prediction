import sqlite3

conn = sqlite3.connect("employees.db")
cur = conn.cursor()

cur.execute("PRAGMA table_info(employee)")
columns = cur.fetchall()

for col in columns:
    print(col)

conn.close()
