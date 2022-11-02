from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

# Initialize blueprint
general = Blueprint("general", __name__)

# Set routes and their rules
@general.route("/")
@login_required
def index():

  # If the current user is authenticated
  if current_user.is_authenticated == True:
    return redirect(url_for("general.courses"))

  # If not, redirect to login
  else:
    return redirect(url_for("auth.login"))

@general.route("/courses")
@login_required
def courses():

  # If the current user is a teacher
  if current_user.UserType == 1:
    return render_template("teacher/courses.html")

  # Else if the current user is a student
  elif current_user.UserType == 0:
    return render_template("student/courses.html")

  # If neither, redirect to login
  else:
    return redirect(url_for("auth.login"))

@general.route("/enrolled_students")
@login_required
def enrolled_students():

  # If the current user is a teacher
  if current_user.UserType == 1:
    return render_template("teacher/enrolled_students.html")
  
  return redirect(url_for("general.index"))

@general.route("/attendance")
@login_required
def attendance():

  # If the current user is a student
  if current_user.UserType == 0:
    return render_template("student/attendance.html")
    
@general.route("/profile")
@login_required
def profile():
  return render_template("general/profile.html")

@general.route("/contact")
def contact():
  return redirect("https://ms.sapientia.ro/hu/a-karrol/elerhetosegek")
