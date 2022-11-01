from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Users(db.Model, UserMixin):
  NeptunCode = db.Column(db.String(6), primary_key=True)
  Email = db.Column(db.String(100), unique=True, nullable=False)
  Password = db.Column(db.String(100), nullable=False)
  FirstName = db.Column(db.String(50), nullable=False)
  LastName = db.Column(db.String(50), nullable=False)
  UserType = db.Column(db.Boolean, default=False)

  def get_id(self):
    return self.NeptunCode

class Courses(db.Model):
  CourseID = db.Column(db.Integer, primary_key=True)
  TeacherCode = db.Column(db.Integer, unique=True, nullable=False)
  Name = db.Column(db.String(50), unique=True, nullable=False)
  Department = db.Column(db.Integer, nullable=False)

class EnrolledStudents(db.Model):
  StudentCode = db.Column(db.Integer, primary_key=True)
  CourseID = db.Column(db.Integer, primary_key=True)
  Approved = db.Column(db.Boolean, default=False)

class CourseDates(db.Model):
  OccasionID = db.Column(db.Integer, primary_key=True)
  CourseID = db.Column(db.Integer, unique=True, nullable=False)
  Type = db.Column(db.Integer, nullable=False)
  Classroom = db.Column(db.Integer, nullable=False)

class Attendance(db.Model):
  CourseID = db.Column(db.Integer, primary_key=True)
  StudentCode = db.Column(db.Integer, primary_key=True)
  Present = db.Column(db.Boolean, default=False)

class Teachers(db.Model):
  NeptunCode = db.Column(db.String(6), primary_key=True)