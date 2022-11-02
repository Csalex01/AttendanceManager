from . import db
from .models import Users, Attendance, CourseDates, Courses, EnrolledStudents, Teachers

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

      # Get user data from the form
      email = request.form.get('email')
      neptun_code = request.form.get("neptun_code")
      first_name = request.form.get("first_name")
      last_name = request.form.get("last_name")
      password = request.form.get("password")
      confirm_password = request.form.get("confirm_password")
      user_type = 0
      
      # Query the teacher's database
      teacher = Teachers.query.filter_by(NeptunCode=neptun_code).first()

      # If there exists a user with the given Neptun code in the teacher's database,
      # the user is a teacher.
      if teacher != None:
        user_type = 1

      # TODO These are only for debugging purposes, remove them when finalising the project.
      print(f"Email: {email}")
      print(f"Neptun Code: {neptun_code}")
      print(f"First Name: {first_name}")
      print(f"Last Name: {last_name}")
      print(f"Password: {password}")
      print(f"Confirm Password: {confirm_password}")
      print(f"User Type: {user_type}")

      # TODO Check for input validity (length, format, etc...)

      # Create the new user
      new_user = Users(
        NeptunCode=neptun_code,
        Email=email,
        Password=password,
        FirstName=first_name,
        LastName=last_name,
        UserType=user_type
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
    return render_template("auth/signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
  # POST request handler
  if request.method == "POST":

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

        # If the password is incorrect, reload the page.
        return redirect(url_for("auth.login"))

    else:

      # If user does not exist, redirect to signup
      return redirect(url_for("auth.login"))

  # GET request handler
  else:
    return render_template("auth/login.html")

# This function is responsible for logging out the user.
@auth.route("/logout")
def logout():
  logout_user()

  # Redirect to general.index
  return redirect(url_for("general.index"))