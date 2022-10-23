from flask import render_template, url_for, flash, redirect, request, Blueprint

# Initialize blueprint
auth = Blueprint("auth", __name__)

# Set routes and their rules
@auth.route("/signup")
def signup():
  return render_template("auth/signup.html")

@auth.route("/login")
def login():
  return render_template("auth/login.html")