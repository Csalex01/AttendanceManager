# Dictionary for departments:
#   The idea is the following.
#   A course can be taught to multiple departments, for example:
#     Physics I: Mechanical Engineering, Mathematics Informatics, Electrical Engineering
#   Each department has a unique numerical identifier. If we want to say that a course is taught to
#   Mechanical Engineering, Mathematics Informatics and Electrical Engineering, we could do bitwise OR
#   operation (or sum) on their identifiers to get a unique number:
#     Mechanical Engineering:    4 - 00000100
#     Mathematics Informatics:  16 - 00010000
#     Electrical Engineering:   32 - 00100000
#                              --------------- OR (SUM)
#                               52 - 00110100


import os

DEPARTMENTS = {
  "APPLIED_LINGUISTICS": 
  {
    "NAME": "Applied Linguistics",
    "ID": 1
  },

  "APPLIED_SOCIAL_SCIENCES": 
  {
    "NAME": "Social Sciences",
    "ID": 2
  },

  "MECHANICAL_ENGINEERING": 
  {
    "NAME": "Mechanical Engineering",
    "ID": 4
  },

  "HORTICULTURE": 
  {
    "NAME": "Horticulture",
    "ID": 8
  },

  "MATHEMATICS_INFORMATICS": 
  {
    "NAME": "Mathematics Informatics",
    "ID": 16
  },

  "ELECTRICAL_ENGINEERING": 
  {
    "NAME": "Electrical Engineering",
    "ID": 32
  }
}

# Dictionary for course types
COURSE_TYPES = {
  "LECTURE": 1,
  "SEMINAR": 2,
  "LAB":  4,
  "PROJECT": 8
}

class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')