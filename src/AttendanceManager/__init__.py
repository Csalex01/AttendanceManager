from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "985230d0ce098c081e5b5b70f9797064"

from AttendanceManager.views import views

app.register_blueprint(views, url_prefix="/")