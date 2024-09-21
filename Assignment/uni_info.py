"""
Question 1. Dictionary
A university wants to create a dictionary to store information about courses, where each key is a
course code, and the value is another dictionary containing details about the course. The details
include the course name, number of credits, and the instructor's name. The university also wants
to perform some operations like updating course details, adding new courses, and removing old
ones.
Write a Python function that performs the following tasks:

1. Create a dictionary with the following courses:
   CSE101: Course name = "Introduction to Programming", Credits = 3, Instructor = "Dr. Alice"
   CSE102: Course name = "Data Structures", Credits = 4, Instructor = "Dr. Bob"
   CSE103: Course name = "Database Systems", Credits = 3, Instructor = "Dr. Carol"

2. Update the instructor's name for CSE102 to "Dr. Bob Jr."

3. Add a new course:
   CSE104: Course name = "Algorithms", Credits = 4, Instructor = "Dr. Dave"

4. Remove the course CSE101 from the dictionary.

5. Loop through the dictionary and print the course code along with its details.
"""


# Initializing a dictionary to store university course information
university_information = {
    "CSE101": {        # nested dictionary
        "Course Name": "Introduction to Programming",
        "Credits": 3,
        'Instructor': "Dr. Alice"
    },
    
    "CSE102": {        # nested dictionary
        "Course Name": "data structures",
        "Credits": 4,
        'Instructor': "Dr. Bob"
    },
    "CSE103": {          # nested dictionary
        "Course Name": "database System",
        "Credits": 3,
        'Instructor': "Dr. Carol"
    }
}

# Printing the initial university information
print(university_information)

# Updating the instructor's name for course CSE102
university_information["CSE102"]["Instructor"] = "Dr. Bob Jr."
print(university_information)

# Adding a new course, CSE104
university_information["CSE104"] = {
    "Course Name": "algorithms",
    "Credits": 4,
    'Instructor': "Dr. Dave"
}
print(university_information)

# Removing course CSE101 from the dictionary
university_information.pop("CSE101")
print(university_information)

# Loop through the dictionary and print each course code along with its details
for course_code, course_details in university_information.items():
    print(f"Course Code: {course_code}")
    print(f"  Course Name: {course_details['Course Name']}")
    print(f"  Credits: {course_details['Credits']}")
    print(f"  Instructor: {course_details['Instructor']}")
    print()