from AttendanceManager import db, app
from AttendanceManager.models import *

from werkzeug.security import generate_password_hash, check_password_hash

from getpass import getpass

from AttendanceManager.helpers import COLORS

# Push application context
ctx = app.app_context()
ctx.push()

# Methods for printing
def print_users():
    users = Users.query.all()

    print(f"\n{COLORS.OKGREEN}Users\n*--------*{COLORS.RESET}")

    for idx, user in enumerate(users):
        print(f"{COLORS.OKCYAN}{idx + 1}. Neptun Code: {user.NeptunCode}{COLORS.RESET}")
        print(f"\tEmail: {user.Email}")
        print(f"\tName: {user.FirstName} {user.LastName}")
        print(f"\tUser type: {'Student' if user.UserType == 0 else 'Teacher'}")
        print("")

def print_teachers():
    teachers = Teachers.query.all()

    print(f"\n{COLORS.OKGREEN}Teachers\n*--------*{COLORS.RESET}")
    for idx, teacher in enumerate(teachers):
        print(f"{COLORS.OKCYAN}{idx + 1}. Neptun Code: {teacher.NeptunCode}{COLORS.RESET}")

    print("")

def print_departments():
    departments = Departments.query.all()

    print(f"\n{COLORS.OKGREEN}Departments\n*--------*{COLORS.RESET}")

    for idx, department in enumerate(departments):
        print(f"{COLORS.OKCYAN}{idx + 1}. DepartmentID: {department.DepartmentID}{COLORS.RESET}")
        print(f"\tName: {department.DepartmentName}")
        print("")

# Methods for inserting into databaase
def signup_user():
    print(f"\n{COLORS.OKGREEN}Sign Up User\n*--------*{COLORS.RESET}")

    neptun_code = input(f"{COLORS.OKCYAN}> Neptun Code:{COLORS.RESET} ")
    email = input(f"{COLORS.OKCYAN}> Email:{COLORS.RESET} ")
    password = getpass(f"{COLORS.OKCYAN}> Password:{COLORS.RESET} ")
    confirm_password = getpass(f"{COLORS.OKCYAN}> Confirm Password:{COLORS.RESET} ")
    first_name = input(f"{COLORS.OKCYAN}> First Name:{COLORS.RESET} ")
    last_name = input(f"{COLORS.OKCYAN}> Last Name:{COLORS.RESET} ")
    user_type = 0

    if password != confirm_password:
        print(f"{COLORS.FAIL}Passwords do not match!{COLORS.RESET}")
        return

    neptun_code_check = Users.query.filter_by(NeptunCode=neptun_code).first()
    email_check = Users.query.filter_by(Email=email).first()

    if neptun_code_check != None:
        print(f"\n{COLORS.FAIL}Neptun code already in use!{COLORS.RESET}")
        return

    if email_check != None:
        print(f"\n{COLORS.FAIL}Email already in use!{COLORS.RESET}")
        return

    teacher = Teachers.query.filter_by(NeptunCode=neptun_code).first()

    if teacher != None:
        user_type = 1

    new_user = Users(
        NeptunCode=neptun_code,
        Email=email,
        Password=password,
        FirstName=first_name,
        LastName=last_name,
        UserType=user_type
    )

    db.session.add(new_user)
    db.session.commit()

# Method for menu
def menu():
    while True:
        print(f"\n{COLORS.OKCYAN}*--------* AttendanceManager Database TUI *--------*{COLORS.RESET}")
        print(f"{COLORS.OKBLUE}*-----------* LOG *-----------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}1.){COLORS.RESET} Print Users")
        print(f"{COLORS.OKGREEN}2.){COLORS.RESET} Print Teachers")
        print(f"{COLORS.OKGREEN}3.){COLORS.RESET} Print Departments")
        print(f"{COLORS.OKBLUE}*-----* Add to Database *-----*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}4.){COLORS.RESET} Sign Up User")
        print(f"{COLORS.OKBLUE}*-----------------------------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}0.){COLORS.RESET} Exit")
        print(f"{COLORS.OKCYAN}*--------------------------------------------------*{COLORS.RESET}")

        try:
            choice = int(input(f"{COLORS.OKGREEN}> Choice: {COLORS.OKCYAN}"))
        except ValueError:
            print(f"\n{COLORS.FAIL}Invalid input! Numbers only.{COLORS.RESET}")
            continue

        if choice == 1:
            print_users()

        elif choice == 2:
            print_teachers()

        elif choice == 3:
            print_departments()

        elif choice == 4:
            signup_user()

        elif choice == 0:
            print("")
            break
        
        else:
            print(f"\n{COLORS.FAIL}Invalid input!{COLORS.RESET}")

menu()

# Pop application context
ctx.pop()