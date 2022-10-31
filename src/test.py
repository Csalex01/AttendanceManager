from AttendanceManager import db, app
from AttendanceManager.models import Users

from werkzeug.security import generate_password_hash, check_password_hash

# Push Application Context
ctx = app.app_context()
ctx.push()

# Test Code
NeptunCode = input("NeptunCode: ")
Email = input("Email: ")
Password = input("Password: ")
FirstName = input("First Name: ")
LastName = input("Last Name: ")
UserType = int(input("User Type (0 - Student, 1 - Teacher): "))

new_user = Users(
  NeptunCode=NeptunCode,
  Email=Email,
  Password=Password,
  FirstName=FirstName,
  LastName=LastName,
  UserType=UserType
)

db.session.add(new_user)
db.session.commit()

# Pop Application Context
ctx.pop()