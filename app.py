from flask import Flask, render_template, request, redirect, url_for
from db_config import get_connection
from flask import flash

app = Flask(__name__)
app.secret_key = "student@manager"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test-db")
def database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return str(results)

@app.route("/students")
def show_students():
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("students.html", students=results)

@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (name, age, major)
        VALUES (%s, %s, %s)
        """, (name, age, major))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Student added successfully!")

        return redirect(url_for("show_students"))

    return render_template("add_student.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        major = request.form["major"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE students
        SET name = %s, age = %s, major = %s
        WHERE id = %s
        """, (name, age, major, id))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Student updated successfully!")

        return redirect(url_for("show_students"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                SELECT *
                FROM students
                WHERE id = %s
                """, (id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("edit_student.html", student=student)

@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE
    FROM students
    WHERE id = %s
    """, (id, ))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Student deleted successfully!")

    return redirect(url_for("show_students"))

if __name__ == "__main__":
    app.run(debug=True)