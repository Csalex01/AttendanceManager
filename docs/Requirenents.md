# Requirements
## User Application Requirements
- For using the application, a web browser either on a smartphone or a PC is required.
- Recommended operating systems (Personal Computer): Windows, Linux, Mac.
- Recommended operating systems (mobile phone): Android, iOS, HarmonyOS.
- For mobile phone users:
	- Camera with the minimum resolution of 4 megapixel (optimal distance: 5m, maximum distance: 20m).
	- Capability of scanning QR codes in the camera application.
- Internet connection.

## Server Application Requirements
- A computer is required for running the server application (preferably Linux operating system).
- A computer with at least 1 GB of storage.
- Python version 3.8.x with the following packages installed (specified in /src/requirements.txt):
	- click v8.1.3
	- Flask v2.2.2
	- Flask-Login v0.6.2
	- Flask-SQLAlchemy v2.5.1
	- greenlet v1.1.3
	- importlib-metadata v4.12.0
	- itsdangerous v2.1.2
	- Jinja2 v3.1.2
	- MarkupSafe v2.1.1
	- SQLAlchemy v1.4.41
	- Werkzeug v2.2.2
	- zipp v3.8.1
- Latest Pip version
- Latest Pipenv version

## Non-functional requirements
- Accessibility, easy navigation.
- Responsive user inerface
- Adaptive user interface on mobile browsers.
- Speed and reliability.

## Functional requirements
Users in general should be able to:
	- Log in,
	- Sign up,
	- Modify their profile data,
	- Navigate between pages.
	- Log out

Users with the role of TEACHER should be able to:
	- See their own courses list,
	- See who is signed up for their courses,
	- Generate a QR code for students to scan,
	- Approve or deny students from course,
	- Mark students as present or absent manually.

Users with the role of STUDENT should be able to:
	- See their signed up courses list,
	- See their attendance in each signed up course,
	- Sign up for courses,
	- Be able to mark themselves as present with the help of a QR code. 

