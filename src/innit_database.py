from AttendanceManager import db, app
from AttendanceManager.models import Teachers, Departments, CourseTypes

from werkzeug.security import generate_password_hash, check_password_hash

# Push Application Context
ctx = app.app_context()
ctx.push()

# Test Code
teacher_1 = Teachers(NeptunCode="ABCDE0")
teacher_2 = Teachers(NeptunCode="FGHIJ1")
teacher_3 = Teachers(NeptunCode="KLMNO2")
teacher_4 = Teachers(NeptunCode="PQRST3")



db.session.add(teacher_1)
db.session.add(teacher_2)
db.session.add(teacher_3)
db.session.add(teacher_4)

#Department Code
APPLIED_LINGUISTICS = Departments(DepartmentID = 1, DepartmentName = "Applied Linguistics")
APPLIED_SOCIAL_SCIENCES = Departments(DepartmentID = 2, DepartmentName = "Social Sciences")
MECHANICAL_ENGINEERING = Departments(DepartmentID = 4, DepartmentName = "Mechanical Engineering")
HORTICULTURE = Departments(DepartmentID = 8, DepartmentName = "Horticulture")
MATHEMATICS_INFORMATICS = Departments(DepartmentID = 16, DepartmentName = "Mathematics Informatics")
ELECTRICAL_ENGINEERING = Departments(DepartmentID = 32, DepartmentName = "Electrical Engineering")

#CourseTypes
LECTURE = CourseTypes(CourseTypeID = 1, CourseTypeName = "Lecture")
SEMINAR = CourseTypes(CourseTypeID = 2, CourseTypeName = "Seminar")
LAB = CourseTypes(CourseTypeID = 4, CourseTypeName = "Lab")
PROJECT = CourseTypes(CourseTypeID = 8, CourseTypeName = "Project")

db.session.commit()

# Pop Application Context
ctx.pop()