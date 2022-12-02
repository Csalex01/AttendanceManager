from AttendanceManager import db, app
from AttendanceManager.models import *

from werkzeug.security import generate_password_hash, check_password_hash

from getpass import getpass
import os

from AttendanceManager.helpers import COLORS, clear_screen

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
        user = Users.query.filter_by(NeptunCode=teacher.NeptunCode).first()

        print(f"{COLORS.OKCYAN}{idx + 1}. Neptun Code: {teacher.NeptunCode}{COLORS.RESET}")

        if user != None:
            print(f"\tEmail: {user.Email}")
            print(f"\tName: {user.FirstName} {user.LastName}")

    print("")

def print_departments():
    departments = Departments.query.all()

    print(f"\n{COLORS.OKGREEN}Departments\n*--------*{COLORS.RESET}")

    for idx, department in enumerate(departments):
        print(f"{COLORS.OKCYAN}{idx + 1}. DepartmentID: {department.DepartmentID}{COLORS.RESET}")
        print(f"\tName: {department.DepartmentName}")
        print("")

def print_courses():
    courses = Courses.query.all()

    print(f"\n{COLORS.OKGREEN}Courses\n*--------*{COLORS.RESET}")

    for idx, course in enumerate(courses):
        teacher = Users.query.filter_by(NeptunCode=course.TeacherCode).first()
        course_type = CourseTypes.query.filter_by(CourseTypeID=course.CourseType).first()

        print(f"{COLORS.OKCYAN}{idx + 1}. CourseID: {course.CourseID}{COLORS.RESET}")
        print(f"\tName: {course.Name}")
        
        print(f"\tTeacher: {course.TeacherCode}")
        if teacher != None:
            print(f"\t\tEmail: {teacher.Email}")
            print(f"\t\tName: {teacher.FirstName} {teacher.LastName}")

        print(f"\tCourse Type: {course_type.CourseTypeName}")

        print("")

# Methods for inserting into databaase
def signup_user():
    print(f"\n{COLORS.OKGREEN}Sign Up User\n*--------*{COLORS.RESET}")

    departments = Departments.query.all()

    print(f"\n{COLORS.OKGREEN}Departments\n*--------*{COLORS.RESET}")

    for idx, department in enumerate(departments):
        print(f"\t{COLORS.OKCYAN}{idx + 1}. {department.DepartmentName} {COLORS.RESET}(ID: {department.DepartmentID})")

    print("")

    try:
        neptun_code = input(f"{COLORS.OKCYAN}> Neptun Code:{COLORS.RESET} ")
        email = input(f"{COLORS.OKCYAN}> Email:{COLORS.RESET} ")
        password = getpass(f"{COLORS.OKCYAN}> Password:{COLORS.RESET} ")
        confirm_password = getpass(f"{COLORS.OKCYAN}> Confirm Password:{COLORS.RESET} ")
        first_name = input(f"{COLORS.OKCYAN}> First Name:{COLORS.RESET} ")
        last_name = input(f"{COLORS.OKCYAN}> Last Name:{COLORS.RESET} ")
        department_id = input(f"{COLORS.OKCYAN}> Department ID:{COLORS.RESET} ")
        user_type = 0

    except KeyboardInterrupt:
        print(f"\n{COLORS.FAIL}\nQuit.{COLORS.RESET}")
        return

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
        DepartmentID=department_id,
        UserType=user_type
    )

    db.session.add(new_user)
    db.session.commit()

    print(f"{COLORS.OKGREEN}\nUser {neptun_code} successfully added to database!{COLORS.RESET}")

def create_course():
    print(f"\n{COLORS.OKGREEN}Create Course\n*--------*{COLORS.RESET}")

    departments = Departments.query.all()
    course_types = CourseTypes.query.all()
    teachers = Teachers.query.all()

    print(f"\n{COLORS.OKGREEN}Departments\n*--------*{COLORS.OKGREEN}")
    for idx, department in enumerate(departments):
        print(f"\t{COLORS.OKCYAN}{idx + 1}. {department.DepartmentName} {COLORS.RESET}(ID: {department.DepartmentID})")

    print(f"\n{COLORS.OKGREEN}Course Types\n*--------*{COLORS.OKGREEN}")
    for idx, course_type in enumerate(course_types):
        print(f"\t{COLORS.OKCYAN}{idx + 1}. {course_type.CourseTypeName} {COLORS.RESET}(ID: {course_type.CourseTypeID})")


    print(f"\n{COLORS.OKGREEN}Teachers\n*--------*{COLORS.RESET}")
    for idx, teacher in enumerate(teachers):
        user = Users.query.filter_by(NeptunCode=teacher.NeptunCode).first()

        print(f"\t{COLORS.OKCYAN}{idx + 1}. {teacher.NeptunCode}{COLORS.RESET}")

        if user != None:
            print(f"\t\tEmail: {user.Email}")
            print(f"\t\tName: {user.FirstName} {user.LastName}")

    print("")

    try:
        course_id = input(f"{COLORS.OKCYAN}> Course ID:{COLORS.RESET} ")
        teacher_code = input(f"{COLORS.OKCYAN}> Teacher's Code:{COLORS.RESET} ")
        name = input(f"{COLORS.OKCYAN}> Name:{COLORS.RESET} ")
        department = int(input(f"{COLORS.OKCYAN}> Department ID:{COLORS.RESET} "))
        course_type = int(input(f"{COLORS.OKCYAN}> Course Type ID:{COLORS.RESET} "))

        course = Courses(
            CourseID=course_id,
            TeacherCode=teacher_code,
            Name=name,
            DepartmentID=department,
            CourseType=course_type
        )

        db.session.add(course)
        db.session.commit()

        print(f"{COLORS.OKGREEN}\nCourse {course_id} successfully added to the database!{COLORS.RESET}")

    except KeyboardInterrupt:
        print(f"\n{COLORS.FAIL}\nQuit.{COLORS.RESET}")
        return    

def create_department():
    print(f"\n{COLORS.OKGREEN}Create Department\n*--------*{COLORS.RESET}")

    last_department_id = Departments.query.all()
    last_department_id = last_department_id[len(last_department_id) - 1].DepartmentID
    print(last_department_id)

    try:
        name = input(f"{COLORS.OKCYAN}> Name:{COLORS.RESET} ")

        department = Departments(
            DepartmentID=last_department_id * 2,
            DepartmentName=name
        )

        db.session.add(department)
        db.session.commit()

    except KeyboardInterrupt:
        print(f"\n{COLORS.FAIL}\nQuit.{COLORS.RESET}")
        return  

# Method for menu
def menu():
    while True:

        print(f"\n{COLORS.OKCYAN}*--------* AttendanceManager Database TUI *--------*{COLORS.RESET}")
        print(f"{COLORS.WARNING}*-----------* LOG *-----------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}1.){COLORS.RESET} Print Users")
        print(f"{COLORS.OKGREEN}2.){COLORS.RESET} Print Teachers")
        print(f"{COLORS.OKGREEN}3.){COLORS.RESET} Print Departments")
        print(f"{COLORS.OKGREEN}4.){COLORS.RESET} Print Courses")
        print(f"{COLORS.WARNING}*-----* Add to Database *-----*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}5.){COLORS.RESET} Sign Up User")
        print(f"{COLORS.OKGREEN}6.){COLORS.RESET} Create Course")
        print(f"{COLORS.OKGREEN}7.){COLORS.RESET} Create Department")
        print(f"{COLORS.WARNING}*-----------------------------*{COLORS.RESET}")
        print(f"{COLORS.OKGREEN}0.){COLORS.RESET} Exit")
        print(f"{COLORS.OKCYAN}*--------------------------------------------------*{COLORS.RESET}")

        try:
            choice = int(input(f"{COLORS.OKGREEN}> Choice: {COLORS.OKCYAN}"))

        except ValueError:
            clear_screen()
            print(f"\n{COLORS.FAIL}Invalid input! Numbers only.{COLORS.RESET}")
            continue

        except KeyboardInterrupt:
            clear_screen()
            print(f"{COLORS.FAIL}\nQuit.{COLORS.RESET}\n")
            return

        clear_screen()

        if choice == 1:
            print_users()

        elif choice == 2:
            print_teachers()

        elif choice == 3:
            print_departments()

        elif choice == 4:
            print_courses()

        elif choice == 5:
            signup_user()

        elif choice == 6:
            create_course()

        elif choice == 7:
            create_department()

        elif choice == 0:
            print(f"{COLORS.FAIL}\nQuit.{COLORS.RESET}\n")
            exit()
        
        else:
            print(f"\n{COLORS.FAIL}Invalid input!{COLORS.RESET}")

# Start the menu
clear_screen()
menu()

# Pop application context
ctx.pop()
