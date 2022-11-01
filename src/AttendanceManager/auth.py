from flask import render_template, url_for, flash, redirect, request, Blueprint

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

      print(f"Email: {email}")
      print(f"Neptun Code: {neptun_code}")
      print(f"First Name: {first_name}")
      print(f"Last Name: {last_name}")
      print(f"Password: {password}")
      print(f"Confirm Password: {confirm_password}")

      # TODO Check for input validity (length, format, etc...)

  return render_template("auth/signup.html")

@auth.route("/login")
def login():
  return render_template("auth/login.html")

@auth.route("/fallback")
def fallback():
  return render_template("general/fallback.html")