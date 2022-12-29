from datetime import datetime
from random import randint

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required

import qrcode

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

        # If the current user is a teacher
        if current_user.UserType == 1:

            # If the user wants to create a new course
            if request.form.get("request_type") == "create_course":

                # Get the course data
                name = request.form.get("course_name")
                departments = request.form.getlist("course_department")

                # Generate course code based on name
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

                # Calculate department flags
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

            # If the user wants to create a new occasion
            elif request.form.get("request_type") == "create_occasion":

                # Get course data
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
                    Date=course_date,
                    Filename=" "
                )

                db.session.add(new_course_date)
                db.session.commit()

                enrolled_students = EnrolledStudents.query.filter_by(CourseID=selected_course).all()

                for student in enrolled_students:
                    if student.Approved == True:
                        attendance = Attendance(
                            OccasionID=new_course_date.OccasionID,
                            StudentCode=student.StudentCode,
                            Present=False
                        )

                        db.session.add(attendance)

                selected_course_code = (Courses.query.filter_by(
                    CourseID=selected_course).first()).CourseCode

                filename = f"{selected_course_code}_{new_course_date.OccasionID}"

                qr_code_img = qrcode.make(
                    f"https://sapientiaattendancemanager.pythonanywhere.com/attend_class?occasion={filename}")

                qr_code_img.save(
                    f"AttendanceManager/static/qr_codes/{filename}.png")

                new_course_date.Filename = f"{filename}"

                db.session.commit()

            elif request.form.get("request_type") == "enroll_students": 
                enrolled_students = EnrolledStudents.query.filter_by(CourseID=selected_course).all()

                for student in enrolled_students:
                    status = request.form.get(student.StudentCode)
                    student.Approved = True if status == "on" else False
                    
                    db.session.add(student)

                db.session.commit()
                
            return redirect(url_for("general.courses", selected_course=selected_course))

        # if the current user is a student
        else:

            # If the user wants to enroll in a course
            if request.form.get("request_type") == "enroll_course":
                course = Courses.query.filter_by(
                    CourseCode=request.form.get("course_code")).first()

                enrolled_student = EnrolledStudents(
                    StudentCode=current_user.NeptunCode,
                    CourseID=course.CourseID,
                    Approved=False
                )

                db.session.add(enrolled_student)
                db.session.commit()

                return redirect(url_for("general.courses", selected_course=selected_course))

    # GET request handler
    elif request.method == "GET":

        # If the current user is a teacher
        if current_user.UserType == 1:

            # Get courses and departments
            courses = Courses.query.filter_by(TeacherCode=current_user.NeptunCode)
            course_types = CourseTypes.query.all()
            departments = Departments.query.all()

            # If the user has courses, but did not select one, select the first course
            if courses.count() != 0 and selected_course == None:
                return redirect(url_for("general.courses", selected_course=courses[0].CourseID))

            # Otherwise get the selected course
            else:
                selected_course = Courses.query.filter_by(CourseID=selected_course).first()

            occasions = []
            enrolled_students = []
            enrolled_student_ids = []
            present_count = []
            attendances = [] 

            # If there is a course selected
            if selected_course != None:

                # Get the occasions and the student ids
                occasions = CourseDates.query.filter_by(
                    CourseID=selected_course.CourseID).all()
                enrolled_student_ids = EnrolledStudents.query.filter_by(
                    CourseID=selected_course.CourseID).all()

                for occasion in occasions:
                    query = Attendance.query.filter_by(OccasionID=occasion.OccasionID, Present=1)
                    present_count.append(query.count())
                    attendances.append(query.all())
                    
                # Get student data based on ids
                enrolled_student_data = []
                for student in enrolled_student_ids:
                    enrolled_student_data.append(Users.query.filter_by(
                        NeptunCode=student.StudentCode).first())

                # Add the student data to a list
                enrolled_students = []
                for i in range(0, len(enrolled_student_data)):
                    enrolled_students.append(
                        [enrolled_student_ids[i], enrolled_student_data[i]])

            return render_template("teacher/courses.html",
                                   courses=courses,
                                   course_types=course_types,
                                   selected_course=selected_course,
                                   occasions=occasions,
                                   departments=departments,
                                   enrolled_students=enrolled_students,
                                   total=len(enrolled_student_ids),
                                   present_count=present_count,
                                   attendances=attendances)

        # Else if the current user is a student
        elif current_user.UserType == 0:

            # Get enrolled courses
            enrolled_courses = EnrolledStudents.query.filter_by(
                StudentCode=current_user.NeptunCode)
            courses = []
            course_types = CourseTypes.query.all()
            occasions = []
            attendance = []
            approved = False

            # Get courses based on enrolled courses
            for course in enrolled_courses:
                courses.append(Courses.query.filter_by(
                    CourseID=course.CourseID).first())

            # If the user is enrolled in courses and there is no selected course
            if enrolled_courses.count() != 0 and selected_course == None:
                # Redirect to general.course with the first enrolled course
                return redirect(url_for("general.courses", selected_course=enrolled_courses[0].CourseID))

            # If the user is enrolled in courses and has selected a course
            elif enrolled_courses.count() != 0 and selected_course != None:
                selected_course = Courses.query.filter_by(
                    CourseID=selected_course).first()

            # Get approved status based on selected course
            if selected_course != None:
                approved = (EnrolledStudents.query.filter_by(
                    StudentCode=current_user.NeptunCode,
                    CourseID=selected_course.CourseID
                ).first()).Approved

                occasions = CourseDates.query.filter_by(CourseID=selected_course.CourseID).all()
                attendance = Attendance.query.filter_by(StudentCode=current_user.NeptunCode).all()

            return render_template("student/courses.html",
                                   courses=courses,
                                   selected_course=selected_course,
                                   approved=approved,
                                   occasions=occasions,
                                   course_types=course_types,
                                   attendance=attendance)

        # If neither, redirect to login
        else:
            return redirect(url_for("auth.login"))


@general.route("/attend_class")
@login_required
def attend_class():

    if request.method == "GET" and current_user.UserType == 0:

        args = (request.args.get("occasion")).split("_")
        course_code = args[0]
        occasion_id = args[1]

        course = Courses.query.filter_by(CourseCode=course_code).first()
        status = EnrolledStudents.query.filter_by(
            CourseID=course.CourseID, 
            StudentCode=current_user.NeptunCode).first()

        if status.Approved == True:
            attendance = Attendance.query.filter_by(
                OccasionID=occasion_id
                ).filter_by(
                    StudentCode=current_user.NeptunCode
                ).first()
            
            if attendance == None:
                return redirect(url_for("general.index"))

            attendance.Present = True

            db.session.add(attendance)
            db.session.commit()

    return redirect(url_for("general.index"))

@general.route("/profile")
@login_required
def profile():
    department = Departments.query.filter_by(
        DepartmentID=current_user.DepartmentID).first()
    study_program = StudyProgram.query.filter_by(
        StudyProgramID=current_user.StudyProgramID).first()

    return render_template("general/profile.html",
                           user=current_user,
                           department=department,
                           study_program=study_program)

@general.route("/contact")
def contact():
    return render_template("general/contact.html")
