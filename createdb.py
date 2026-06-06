import sqlite3

db = sqlite3.connect("employees.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE employee(
    id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    satisfaction REAL,
    evaluation REAL,
    projects INTEGER,
    hours INTEGER,
    experience INTEGER,
    performance TEXT,
    base_salary INTEGER,
    appraisal_percentage INTEGER,
    final_salary INTEGER
)
""")

db.commit()
db.close()

print("Fresh database created successfully!")
