from flask import Flask, render_template

from storage import Student

app = Flask(
    __name__,
    static_url_path="/assets",
)


@app.get("/")
def get_home():
    return render_template("index.html")


@app.get("/students")
def get_students():
    students = Student.all()
    return render_template("students.html", students=students)


@app.get("/students/<int:student_id>")
def get_student(student_id):
    res =Student.exec(student_id)
    return render_template("student_info.html", student_info=res )

@app.get("/about")
def get_about_us():
    return render_template("about.html")


@app.get("/contacts")
def get_contacts_page():
    return render_template("contacts.html")


# @app.get("/favicon.ico")
# def get_favicon():
#     return app.send_static_file("favicon.ico")


if __name__ == "__main__":
    app.run(port=5001)
