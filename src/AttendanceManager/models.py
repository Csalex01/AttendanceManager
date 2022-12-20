from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Model for Users
class Users(db.Model, UserMixin):
    NeptunCode = db.Column(db.String(6), primary_key=True)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    UserType = db.Column(db.Boolean, default=False)
    DepartmentID = db.Column(db.Integer, nullable=False)
    StudyProgramID = db.Column(db.Integer)

    # This is required for getting the ID (NeptunCode) to log the user in
    def get_id(self):
        return self.NeptunCode

# Model for Courses
class Courses(db.Model):
    CourseID = db.Column(db.Integer, primary_key=True)
    CourseCode = db.Column(db.String(10), unique=True)
    TeacherCode = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(50), unique=True, nullable=False)
    DepartmentID = db.Column(db.Integer, nullable=False)

# Model for Enrolled Students
class EnrolledStudents(db.Model):
    StudentCode = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, primary_key=True)
    Approved = db.Column(db.Boolean, default=False)

# Model for Course Dates (when is a course held with a given type)
class CourseDates(db.Model):
    OccasionID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, unique=False, nullable=False)
    Type = db.Column(db.Integer, nullable=False)
    Classroom = db.Column(db.Integer, nullable=False)
    CourseType = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.String, nullable=False)
    Filename = db.Column(db.String, nullable=False)

# Model for Student Attendance
class Attendance(db.Model):
    OccasionID = db.Column(db.Integer, primary_key=True)
    StudentCode = db.Column(db.Integer, primary_key=True)
    Present = db.Column(db.Boolean, default=False)

# Model for Teachers (used at user registration to decide the user type)
class Teachers(db.Model):
    NeptunCode = db.Column(db.String(6), primary_key=True)

# Model for Departments
class Departments(db.Model):
    DepartmentID = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(50), unique=True, nullable=False)

# Model for Study Program
class StudyProgram(db.Model):
    StudyProgramID = db.Column(db.Integer, primary_key=True)
    DepartmentID = db.Column(db.Integer, nullable=False)
    StudyProgramName = db.Column(db.String(50), unique=True, nullable=False)

# Model for CourseTypes
class CourseTypes(db.Model):
    CourseTypeID = db.Column(db.Integer, primary_key=True)
    CourseTypeName = db.Column(db.String(10), nullable=False)
