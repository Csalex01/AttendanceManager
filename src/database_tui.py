from AttendanceManager import db, app
from AttendanceManager.models import *

from werkzeug.security import generate_password_hash, check_password_hash

# Push application context
ctx = app.app_context()
ctx.push()

# Helper functions


def print_users():
    users = Users.query.all()

    print("\nUsers\n----------")

    for idx, user in enumerate(users):
        print(f"{idx + 1}. Neptun Code: {user.NeptunCode}")
        print(f"\tEmail: {user.Email}")
        print(f"\tName: {user.FirstName} {user.LastName}")
        print(f"\tUser type: {'Student' if user.UserType == 0 else 'Teacher'}")
        print("")


def print_teachers():
    teachers = Teachers.query.all()

    print("\nTeachers\n----------")
    for idx, teacher in enumerate(teachers):
        print(f"{idx + 1}. {teacher.NeptunCode}")

    print("")


def print_departments():
    departments = Departments.query.all()

    print("\nDepartments\n----------")

    for idx, department in enumerate(departments):
        print(f"{idx + 1}. DepartmentID: {department.DepartmentID}")
        print(f"\tName: {department.DepartmentName}")
        print("")


def menu():
    while True:
        print("\n---------- AttendanceManager Database TUI ----------")
        print("1.) Print Users")
        print("2.) Print Teachers")
        print("3.) Print Departments")
        print("0.) Exit")
        print("----------------------------------------------------")

        choice = int(input("> Choice: "))

        if choice == 1:
            print_users()

        elif choice == 2:
            print_teachers()

        elif choice == 3:
            print_departments()

        elif choice == 0:
            break


menu()

# Pop application context
ctx.pop()
