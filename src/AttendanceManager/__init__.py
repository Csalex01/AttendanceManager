from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize app with the current package name
app = Flask(__name__)

# Secret key for encryption
app.config["SECRET_KEY"] = "985230d0ce098c081e5b5b70f9797064"

# Import blueprints
from AttendanceManager.general import general
from AttendanceManager.auth import auth

# Register blueprints
app.register_blueprint(general, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")