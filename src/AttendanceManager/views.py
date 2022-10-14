from flask import render_template, url_for, flash, redirect, request, Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def index():
  return render_template("views/index.html")