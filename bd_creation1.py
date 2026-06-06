import sqlite3

conn = sqlite3.connect("employees.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS employee")

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

conn.commit()
conn.close()

print("Fresh database created successfully")
