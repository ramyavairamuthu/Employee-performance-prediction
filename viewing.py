import sqlite3

conn = sqlite3.connect("employees.db")  # replace with your DB file
cur = conn.cursor()

# Show columns and table info
cur.execute("PRAGMA table_info(employee)")
print(cur.fetchall())

# Show all rows
cur.execute("SELECT * FROM employee")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
