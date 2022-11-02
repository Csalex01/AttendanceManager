from AttendanceManager import db, app
from AttendanceManager.models import Teachers

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

db.session.commit()

# Pop Application Context
ctx.pop()