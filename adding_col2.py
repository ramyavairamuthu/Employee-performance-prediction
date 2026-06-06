import sqlite3

conn = sqlite3.connect("employees.db")
cur = conn.cursor()

cur.execute("ALTER TABLE employee ADD COLUMN base_salary INTEGER")
cur.execute("ALTER TABLE employee ADD COLUMN final_salary INTEGER")

conn.commit()
conn.close()

print("Salary columns added successfully")
