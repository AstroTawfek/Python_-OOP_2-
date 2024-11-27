"""
Scenario: 
You are given a dataset of students' scores in different subjects stored in a 2D NumPy
array, where each row represents a student and each column represents a subject. You need to
calculate the average score per student and identify the student with the highest average.

Question:
Write a Python function using NumPy to calculate the average score for each student. Then,
identify the student with the highest average score and print their score. Use appropriate NumPy
functions to solve this problem efficiently.

"""

import numpy as np

def find_highest_average_student(scores):
    # Calculating the average score for each student
    average_scores = np.mean(scores, axis=1)
    
    # Identifying the index of the student with the highest average score
    highest_avg_index = np.argmax(average_scores)
    
    # Getting the highest average score
    highest_average_score = average_scores[highest_avg_index]
    
    # Printing the highest average score
    print(f"The highest average score is {highest_average_score} for student index {highest_avg_index}.")
    
    return highest_average_score

scores = np.array([[80, 90, 85], 
                   [70, 75, 80], 
                   [90, 95, 100]])

find_highest_average_student(scores)