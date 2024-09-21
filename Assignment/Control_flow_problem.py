'''
Question 4. Control flow
You are developing a program for a school to analyze student grades and categorize them based
on their performance. The grades are stored in an array, and the school uses the following
grading scheme:
 Grade A: Score above 80
 Grade B: Score between 60 and 80
 Grade C: Score between 40 and 60
 Grade F: Score below 40
You are given an array of student grades:
grades = [85, 78, 92, 45, 33, 67, 88, 41]
Perform the following tasks:
    a. Use a for loop with if-else conditions to categorize each student's grade and display their grade
category (A, B, C, or F).
    b. Implement a function called boost_grades that increases each student's grade by 5%. Use the
map() function to apply this adjustment to the grades array and print the new grades.

    c. Use a lambda function to find which students' boosted grades are now above 90 and print
those grades.
Write the Python code that solves the problem, and show the final output.

Expected output:
Grade Categories:
Score: 85 - Grade: A
Score: 78 - Grade: B
Score: 92 - Grade: A
Score: 45 - Grade: C
Score: 33 - Grade: F
Score: 67 - Grade: B
Score: 88 - Grade: A
Score: 41 - Grade: C

Boosted Grades:
[89.25, 81.9, 96.6, 47.25, 34.65, 70.35, 92.4, 43.05]

Boosted Grades Above 90:
[96.6, 92.4]
'''

grades = [85, 78, 92, 45, 33, 67, 88, 41]


def students_grade_analyze(grades):
    for score in grades:
        if score >= 80:
            print(f"Score: {score} - Grade: A")
        elif score>=60 :
            print(f"Score: {score} - Grade: B")
        elif score>=40 :
            print(f"Score: {score} - Grade: C")
        else:
            print(f"Score: {score} - Grade: F")
   
    boosted_grades = boost_grades(grades)
    print(f'Boosted Grades : {boosted_grades}')

    print('Boosted Grades Above 90 :',above_90(boosted_grades))

def boost_grades(grades):
    boosted_grades = list(map(grade_boosting, grades))
    return boosted_grades

def grade_boosting(x):
    return round(x * 1.05 , 2)

def above_90(grades):
    new_grades= list(filter(lambda x : x>90 , grades))
    return new_grades

students_grade_analyze(grades)