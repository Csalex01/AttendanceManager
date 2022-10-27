from flask import render_template, url_for, flash, redirect, request, Blueprint

# Initialize blueprint
general = Blueprint("general", __name__)

user_role = "student"

# Set routes and their rules
@general.route("/")
def index():
  if user_role == "teacher":
    return render_template("teacher/index.html")
  elif user_role == "student":
    return render_template("student/index.html")
  else:
    return render_template("general/fallback.html")

@general.route("/courses")
def courses():
  if user_role == "teacher":
    return render_template("teacher/courses.html")
  elif user_role == "student":
    return render_template("student/courses.html")
  else:
    return render_template("general/fallback.html")

@general.route("/enrolled_students")
def enrolled_students():
  if user_role == "teacher":
    return render_template("teacher/enrolled_students.html")
  
  return redirect(url_for("general.index"))

@general.route("/attendance")
def attendance():
  if user_role == "student":
    return render_template("student/attendance.html")

@general.route("/profile")
def profile():
  return render_template("general/profile.html")

@general.route("/contact")
def contact():
  return redirect("https://ms.sapientia.ro/hu/a-karrol/elerhetosegek")

@general.route("/logout")
def logout():
  pass