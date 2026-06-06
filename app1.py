from flask import Flask, render_template, request, redirect
import sqlite3
import pickle
import numpy as np
import re

app = Flask(
    __name__,
    template_folder="templates1",
    static_folder="static1"
)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))

def get_db():
    return sqlite3.connect("employees.db")

# ---------------- DASHBOARD ----------------
@app.route("/")
def dashboard():
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT COUNT(*) FROM employee")
    total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM employee WHERE performance='High'")
    high = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM employee WHERE performance='Low'")
    low = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM employee WHERE performance='Not Predicted'")
    pending = cur.fetchone()[0]

    return render_template(
        "dashboard1.html",
        total=total,
        high=high,
        low=low,
        pending=pending
    )


# ---------------- ADD EMPLOYEE ----------------
@app.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        data = request.form
        emp_id = data["id"].strip()

        # 🔹 1. Format Validation (E followed by 3 digits)
        if not re.match(r"^E\d{3}$", emp_id):
            return "Invalid Employee ID format! Use format like E101."

        db = get_db()
        cur = db.cursor()

        # 🔹 2. Duplicate ID Validation
        cur.execute("SELECT * FROM employee WHERE id=?", (emp_id,))
        existing = cur.fetchone()

        if existing:
            return "Employee ID already exists!"

        # 🔹 3. Insert if validation passed
        cur.execute("""
        INSERT INTO employee
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            emp_id,
            data["name"],
            data["department"],
            float(data["satisfaction"]),
            float(data["evaluation"]),
            int(data["projects"]),
            int(data["hours"]),
            int(data["experience"]),
            "Not Predicted",
            int(data["salary"]),
            0,
            0
        ))

        db.commit()
        return redirect("/view")

    return render_template("add_employee1.html")
# ---------------- VIEW ----------------
@app.route("/view")
def view_employee():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    return render_template("view_employee1.html", rows=rows)

# ---------------- DELETE ----------------
@app.route("/delete/<id>")
def delete_employee(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    db.commit()
    return redirect("/view")

# ---------------- PREDICT ----------------
@app.route("/predict/<id>")
def predict(id):

    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM employee WHERE id=?", (id,))
    emp = cur.fetchone()

    X = np.array([[emp[3], emp[4], emp[5], emp[6], emp[7]]])

    result = model.predict(X)[0]

    base_salary = emp[9]

    if result == "High":
        appraisal = 20

    elif result == "Average":
        appraisal = 10

    else:
        appraisal = 5

    final_salary = base_salary + (base_salary * appraisal // 100)

    cur.execute("""
        UPDATE employee
        SET performance=?, appraisal_percentage=?, final_salary=?
        WHERE id=?
    """, (result, appraisal, final_salary, id))

    db.commit()

    return redirect("/report")
# ---------------- REPORT ----------------
@app.route("/report")
def report():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT * FROM employee
        WHERE performance != 'Not Predicted'
    """)
    rows = cur.fetchall()
    return render_template("report1.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
