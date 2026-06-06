import sqlite3

conn = sqlite3.connect("employees.db")
cur = conn.cursor()

cur.execute("""
ALTER TABLE employee
ADD COLUMN appraisal_percentage INTEGER
""")

conn.commit()
conn.close()

print("Column added successfully")
