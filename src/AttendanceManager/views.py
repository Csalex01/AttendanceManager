from flask import render_template, url_for, flash, redirect, request, Blueprint

# Initialize blueprint
views = Blueprint("views", __name__)

# Set routes and their rules
@views.route("/")
def index():
  return render_template("views/index.html")