import sqlite3

conn = sqlite3.connect("employees.db")
cur = conn.cursor()

cur.execute("SELECT * FROM employee")
rows = cur.fetchall()

for r in rows:
    print(r)
