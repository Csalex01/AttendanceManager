from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

# Initialize blueprint
general = Blueprint("general", __name__)

# Set routes and their rules
@general.route("/")
@login_required
def index():
  if current_user.UserType == 1:
    return render_template("teacher/index.html")
  elif current_user.UserType == 0:
    return render_template("student/index.html")
  else:
    return redirect(url_for("auth.login"))

@general.route("/courses")
@login_required
def courses():
  if current_user.UserType == 1:
    return render_template("teacher/courses.html")
  elif current_user.UserType == 0:
    return render_template("student/courses.html")
  else:
    return redirect(url_for("auth.login"))

@general.route("/enrolled_students")
@login_required
def enrolled_students():
  if current_user.UserType == 1:
    return render_template("teacher/enrolled_students.html")
  
  return redirect(url_for("general.index"))

@general.route("/attendance")
@login_required
def attendance():
  if current_user.UserType == 0:
    return render_template("student/attendance.html")
    
@general.route("/profile")
@login_required
def profile():
  return render_template("general/profile.html")

@general.route("/contact")
def contact():
  return redirect("https://ms.sapientia.ro/hu/a-karrol/elerhetosegek")
