import sqlite3

db = sqlite3.connect("employees.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE employee(
id TEXT PRIMARY KEY,
name TEXT,
department TEXT,
salary TEXT,
satisfaction REAL,
evaluation REAL,
projects INTEGER,
hours INTEGER,
experience INTEGER,
performance TEXT
)
""")

db.commit()
db.close()
