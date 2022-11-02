from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path

# Initialize app with the current package name
app = Flask(__name__)

# Create database
db = SQLAlchemy()
DB_NAME = "database.db"

# Secret key for encryption
app.config["SECRET_KEY"] = "985230d0ce098c081e5b5b70f9797064"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Import blueprints
from AttendanceManager.general import general
from AttendanceManager.auth import auth

# Register blueprints
app.register_blueprint(general, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")

# Import models
from .models import Users, Courses, EnrolledStudents

# Initialize Database
db.init_app(app=app)

# Create .db file if it does not exist.
if not path.exists(f"AttendanceManager/{DB_NAME}"):
  db.create_all(app=app)
  print("DATABASE CREATED!")

# Create login manager
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "danger"
login_manager.init_app(app)

# THis function is responsible for fetching the current user from the database
@login_manager.user_loader
def load_user(NeptunCode):
  return Users.query.get(NeptunCode)