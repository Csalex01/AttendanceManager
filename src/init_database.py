from AttendanceManager import db, app
from AttendanceManager.models import *

from werkzeug.security import generate_password_hash, check_password_hash


def init_database():

    # Push Application Context
    ctx = app.app_context()
    ctx.push()

    # Teachers
    teacher_1 = Teachers(NeptunCode="ABCDE0")
    teacher_2 = Teachers(NeptunCode="FGHIJ1")
    teacher_3 = Teachers(NeptunCode="KLMNO2")
    teacher_4 = Teachers(NeptunCode="PQRST3")

    db.session.add(teacher_1)
    db.session.add(teacher_2)
    db.session.add(teacher_3)
    db.session.add(teacher_4)

    # Departments
    APPLIED_LINGUISTICS = Departments(
        DepartmentID=1, DepartmentName="Applied Linguistics")
    APPLIED_SOCIAL_SCIENCES = Departments(
        DepartmentID=2, DepartmentName="Social Sciences")
    MECHANICAL_ENGINEERING = Departments(
        DepartmentID=4, DepartmentName="Mechanical Engineering")
    HORTICULTURE = Departments(DepartmentID=8, DepartmentName="Horticulture")
    MATHEMATICS_INFORMATICS = Departments(
        DepartmentID=16, DepartmentName="Mathematics Informatics")
    ELECTRICAL_ENGINEERING = Departments(
        DepartmentID=32, DepartmentName="Electrical Engineering")

    db.session.add(APPLIED_LINGUISTICS)
    db.session.add(APPLIED_SOCIAL_SCIENCES)
    db.session.add(MECHANICAL_ENGINEERING)
    db.session.add(HORTICULTURE)
    db.session.add(MATHEMATICS_INFORMATICS)
    db.session.add(ELECTRICAL_ENGINEERING)

    #StudyProgram
    HORTICULTURAL_ENGINEERING = StudyProgram(
        StudyProgramID=1, DepartmentID=8, StudyProgramName="Horticultural Engineering")
    AUTOMATION_AND_APPLIED_INFORMATICS = StudyProgram(
        StudyProgramID=2, DepartmentID=32, StudyProgramName="Automation and Applied Informatics")
    COMPUTER_SCIENCE = StudyProgram(
        StudyProgramID=3, DepartmentID=32, StudyProgramName="Computer Science")
    COMMUNICATION_AND_PUBLIC_RELATIONS = StudyProgram(
        StudyProgramID=4, DepartmentID=2, StudyProgramName="Communication and Public Relations")
    INFORCMATICS = StudyProgram(
        StudyProgramID=5, DepartmentID=32, StudyProgramName="Informatics")
    LANDSCAPE_ARCHITECTURE = StudyProgram(
        StudyProgramID=6, DepartmentID=8, StudyProgramName="Landscape Architecture")
    MACHINE_MANUFACTURINIG_ENGINEERING = StudyProgram(
        StudyProgramID=7, DepartmentID=16, StudyProgramName="Machine Manufacturinig Engineering")
    MECHATRONICS = StudyProgram(
        StudyProgramID=8, DepartmentID=16, StudyProgramName="Mechatronics")
    PUBLIC_HEALTH_SYSTEMS_AND_TECHNOLOGIES = StudyProgram(
        StudyProgramID=9, DepartmentID=2, StudyProgramName="Public Health Services and Policies")
    TELECOMMUNICATION_SYSTEMS_AND_TECHNOLOGIES = StudyProgram(
        StudyProgramID=10, DepartmentID=32, StudyProgramName="Telecommunication Systems and Technologies")
    TRANSLATEION_AND_INTERPRETING_STUDIES = StudyProgram(
        StudyProgramID=11, DepartmentID=1, StudyProgramName="Translateion and Interpreting Studies")

    db.session.add(HORTICULTURAL_ENGINEERING)
    db.session.add(AUTOMATION_AND_APPLIED_INFORMATICS)
    db.session.add(COMMUNICATION_AND_PUBLIC_RELATIONS)
    db.session.add(INFORCMATICS)
    db.session.add(LANDSCAPE_ARCHITECTURE)
    db.session.add(MACHINE_MANUFACTURINIG_ENGINEERING)
    db.session.add(MECHATRONICS)
    db.session.add(PUBLIC_HEALTH_SYSTEMS_AND_TECHNOLOGIES)
    db.session.add(TELECOMMUNICATION_SYSTEMS_AND_TECHNOLOGIES)
    db.session.add(TRANSLATEION_AND_INTERPRETING_STUDIES)

    

    # CourseTypes
    LECTURE = CourseTypes(CourseTypeID=1, CourseTypeName="Lecture")
    SEMINAR = CourseTypes(CourseTypeID=2, CourseTypeName="Seminar")
    LAB = CourseTypes(CourseTypeID=4, CourseTypeName="Lab")
    PROJECT = CourseTypes(CourseTypeID=8, CourseTypeName="Project")

    db.session.add(LECTURE)
    db.session.add(SEMINAR)
    db.session.add(LAB)
    db.session.add(PROJECT)

    # Commit to database
    db.session.commit()

    # Pop Application Context
    ctx.pop()
