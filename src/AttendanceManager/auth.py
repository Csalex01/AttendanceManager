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
  if request.method == "POST":
      email = request.form.get('email')
      neptun_code = request.form.get("neptun_code")
      first_name = request.form.get("first_name")
      last_name = request.form.get("last_name")
      password = request.form.get("password")
      confirm_password = request.form.get("confirm_password")
      user_type = 0
      
      teacher = Teachers.query.filter_by(NeptunCode=neptun_code).first()

      if teacher != None:
        user_type = 1

      print(f"Email: {email}")
      print(f"Neptun Code: {neptun_code}")
      print(f"First Name: {first_name}")
      print(f"Last Name: {last_name}")
      print(f"Password: {password}")
      print(f"Confirm Password: {confirm_password}")
      print(f"User Type: {user_type}")

      # TODO Check for input validity (length, format, etc...)

      new_user = Users(
        NeptunCode=neptun_code,
        Email=email,
        Password=password,
        FirstName=first_name,
        LastName=last_name,
        UserType=user_type
      )

      db.session.add(new_user)
      db.session.commit()

      login_user(new_user, remember=True)

      return redirect(url_for("general.index"))

  else:
    return render_template("auth/signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")

    user = Users.query.filter_by(Email=email).first()

    if user:
      if password == user.Password:
        login_user(user, remember=True)
        print(user)
        return redirect(url_for("general.index"))
      else:
        return redirect(url_for("auth.login"))

  else:
    return render_template("auth/login.html")

@auth.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("general.index"))