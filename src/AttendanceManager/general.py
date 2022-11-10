from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

from AttendanceManager.models import *

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
    courses = ["Physics II", "Electronics II.", "Databases I."]

    return render_template("student/courses.html", courses=courses)

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

@general.route("/profile")
@login_required
def profile():
  department = Departments.query.filter_by(DepartmentID=current_user.DepartmentID).first()
  study_program = StudyProgram.query.filter_by(StudyProgramID=current_user.StudyProgramID).first()

  return render_template("general/profile.html", 
    user=current_user,
    department=department,
    study_program=study_program
  )

@general.route("/contact")
def contact():
 return render_template("general/contact.html")
