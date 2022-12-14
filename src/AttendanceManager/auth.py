from . import db
from .models import *

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_user, logout_user

# Initialize blueprint
auth = Blueprint("auth", __name__)
general = Blueprint("general", __name__)

# Set routes and their rules
@auth.route("/signup", methods=["GET", "POST"])
def signup():

  # POST request handler
  if request.method == "POST":
      # Create a dictionary with possible errors
      errors = {
        "WRONG_EMAIL": False,
        "WRONG_PASSWORD": False,
        "WRONG_NEPTUN_CODE": False,
        "WRONG_FIRST_NAME": False,
        "WRONG_LAST_NAME": False,
        "DEPARTMENT_DNE": False,
        "STUDY_PROGRAM_DNE": False,
        "PASSWORD_CONF": False,
        "EMPTY_FIELDS": False
      }
      
      found_errors = False
      
      # Get user data from the form
      email = request.form.get('email')
      neptun_code = request.form.get("neptun_code")
      first_name = request.form.get("first_name")
      last_name = request.form.get("last_name")
      password = request.form.get("password")
      confirm_password = request.form.get("confirm_password")
      department = request.form.get("department")
      study_program = request.form.get("study_program")
      user_type = 0
      
      # Query the teacher's database
      teacher = Teachers.query.filter_by(NeptunCode=neptun_code).first()

      # If there exists a user with the given Neptun code in the teacher's database,
      # the user is a teacher.
      if teacher != None:
        user_type = 1

      if len(email) < 1 and len(neptun_code) < 1 and len(first_name) < 1 and len(last_name) < 1 and len(password) < 1 and department == None and study_program == None:
        flash("All fields must be filled!")
        errors = {
          "WRONG_EMAIL": True,
          "WRONG_PASSWORD": True,
          "WRONG_NEPTUN_CODE": True,
          "WRONG_FIRST_NAME": True,
          "WRONG_LAST_NAME": True,
          "DEPARTMENT_DNE": True,
          "STUDY_PROGRAM_DNE": True,
          "PASSWORD_CONF": True,
          "EMPTY_FIELDS": True
        }
        
        departments = Departments.query.all()
        study_programs = StudyProgram.query.all()

        return render_template(
          "auth/signup.html", 
          departments=departments, 
          study_programs=study_programs,
          errors=errors
        )

      if len(email) < 5:
        flash("Email must be at least 5 characters long.")
        errors["WRONG_EMAIL"] = True

      if len(neptun_code) < 6:
        flash("Neptun code must be 6 characters long.")
        errors["WRONG_NEPTUN_CODE"] = True
        found_errors = True

      if len(first_name) < 2:
        flash("First name is too short.")
        errors["WRONG_FIRST_NAME"] = True
        found_errors = True

      if len(last_name) < 2:
        flash("Last name is too short.")
        errors["WRONG_LAST_NAME"] = True
        found_errors = True

      if password != confirm_password:
        flash("Passwords do not match.")
        errors["PASSWORD_CONF"] = True
        found_errors = True

      if department == None:
        flash("Please select a department.")
        errors["DEPARTMENT_DNE"] = True
        found_errors = True

      if user_type == 0 and study_program == None:
        flash("Please select a study program")
        errors["STUDY_PROGRAM_DNE"] = True
        found_errors = True

      if found_errors == True:
        departments = Departments.query.all()
        study_programs = StudyProgram.query.all()

        return render_template(
          "auth/signup.html", 
          departments=departments, 
          study_programs=study_programs,
          errors=errors
        )

      # Create the new user
      new_user = Users(
        NeptunCode=neptun_code,
        Email=email,
        Password=password,
        FirstName=first_name,
        LastName=last_name,
        UserType=user_type,
        DepartmentID=department,
        StudyProgramID=study_program
      )

      # Add new user to the session
      db.session.add(new_user)

      # Commit the session
      db.session.commit()

      # Log in the user
      login_user(new_user, remember=True)

      # Redirect to general.index
      return redirect(url_for("general.index"))

  # GET request handler
  else:
    departments = Departments.query.all()
    study_programs = StudyProgram.query.all()

    return render_template(
      "auth/signup.html", 
      departments=departments, 
      study_programs=study_programs
    )

@auth.route("/login", methods=["GET", "POST"])
def login():

  # POST request handler
  if request.method == "POST":

    # Create a dictionary with possible errors
    errors = {
      "WRONG_EMAIL": False,
      "WRONG_PASSWORD": False
    }

    # Get user data from the form
    email = request.form.get("email")
    password = request.form.get("password")

    # Query the database and filter by email
    user = Users.query.filter_by(Email=email).first()

    # If the user exists in the database
    if user:
      
      # Then check if the password is correct
      if password == user.Password:
        # Log in the user
        login_user(user, remember=True)
        
        # Redirect to general.index
        return redirect(url_for("general.index"))
      else:

        # If the password is incorrect, reload the page with an error.
        flash("Wrong password!")
        errors["WRONG_PASSWORD"] = True

        return render_template("auth/login.html", errors=errors)
    else:

      # If user does not exist, redirect to signup
      flash(f"There is no such user {email}")
      errors["WRONG_EMAIL"] = True

      return render_template("auth/login.html", errors=errors)

  # GET request handler
  else:
    return render_template("auth/login.html")

# This function is responsible for logging out the user.
@auth.route("/logout")
def logout():
  logout_user()

  # Redirect to general.index
  return redirect(url_for("auth.login"))