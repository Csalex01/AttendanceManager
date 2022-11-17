from datetime import datetime
from random import randint

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

from AttendanceManager.models import *

# Initialize blueprint
general = Blueprint("general", __name__)

# Set routes and their rules
@general.route("/")
@login_required
def index():

  # If the current user is authenticated
  if current_user.is_authenticated == True:
    return redirect(url_for("general.courses"))

  # If not, redirect to login
  else:
    return redirect(url_for("auth.login"))

@general.route("/courses", methods=["GET", "POST"])
@login_required
def courses():

    # Get the selected course
    selected_course = request.args.get("selected_course")
    # print(selected_course)

    # POST request handler
    if request.method == "POST":
        if current_user.UserType == 1:

            if request.form.get("request_type") == "create_course":
                name = request.form.get("course_name")
                departments = request.form.getlist("course_department")

                course_code = name.replace('.', '')
                course_code = course_code.split(" ")
                
                generated_code = ""

                for idx, token in enumerate(course_code):
                  if idx > 2:
                    break
                  
                  generated_code = generated_code + token[0:3]

                n = len(generated_code)
                for i in range(0, 10 - n):
                    generated_code = generated_code + str(randint(0, 9))

                print(generated_code)

                sum = 0
                for department in departments:
                  sum = sum + int(department)

                new_course = Courses(
                    TeacherCode=current_user.NeptunCode,
                    Name=name,
                    DepartmentID=sum,
                    CourseCode=generated_code
                )

                db.session.add(new_course)
                db.session.commit()

            elif request.form.get("request_type") == "create_occasion":
                course_type = int(request.form.get("course_type")) - 1
                classroom = request.form.get("classroom")
                course_date = request.form.get("course_date")
                course_time = request.form.get("course_time")

                course_date += f" {course_time}"

                new_course_date = CourseDates(
                  CourseID=selected_course,
                  Type=course_type,
                  Classroom=classroom,
                  CourseType=course_type,
                  Date=course_date
                )

                db.session.add(new_course_date)
                db.session.commit()

        return redirect(url_for("general.index"))

    # GET request handler
    elif request.method == "GET":

        # If the current user is a teacher
        if current_user.UserType == 1:
            courses = Courses.query.filter_by(TeacherCode=current_user.NeptunCode)
            course_types = CourseTypes.query.all()
            departments = Departments.query.all()

            # If the user has courses, but did not select one, select the first course
            if courses.count() != 0 and selected_course == None:
              return redirect(url_for("general.courses", selected_course=courses[0].CourseID))

            # Otherwise get the selected course
            else:
              selected_course = Courses.query.filter_by(CourseID=selected_course).first()

            occasions = None

            if selected_course != None:
              occasions = CourseDates.query.filter_by(CourseID=selected_course.CourseID)

            return render_template("teacher/courses.html", 
                courses=courses, 
                course_types=course_types, 
                selected_course=selected_course,
                occasions=occasions,
                departments=departments)

        # Else if the current user is a student
        elif current_user.UserType == 0:
            enrolled_courses = EnrolledStudents.query.filter_by(StudentCode=current_user.NeptunCode)
            courses = []

            for course in enrolled_courses:
              courses.append(Courses.query.filter_by(CourseID=course.CourseID).first())

            return render_template("student/courses.html", 
                courses=courses, 
                selected_course=selected_course
            )

        # If neither, redirect to login
        else:
            return redirect(url_for("auth.login"))

@general.route("/enrolled_students")
@login_required
def enrolled_students():

  # If the current user is a teacher
  if current_user.UserType == 1:
    return render_template("teacher/enrolled_students.html")
  
  return redirect(url_for("general.index"))

@general.route("/profile")
@login_required
def profile():
  department = Departments.query.filter_by(DepartmentID=current_user.DepartmentID).first()
  study_program = StudyProgram.query.filter_by(StudyProgramID=current_user.StudyProgramID).first()

  return render_template("general/profile.html", 
    user=current_user,
    department=department,
    study_program=study_program
  )

@general.route("/contact")
def contact():
 return render_template("general/contact.html")
