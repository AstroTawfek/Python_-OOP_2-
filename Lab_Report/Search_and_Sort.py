"""
Scenario: You have a dataset representing student scores in various exams stored in an array.
You need to locate specific scores and arrange the data in ascending or descending order.

Question:
Given a 1D NumPy array of scores, write code to:
● Search for specific scores (e.g., 75 and 90) and return their indices.
● Sort the array in ascending and descending order.
Demonstrate both operations and provide examples.

"""


import numpy as np

# Example dataset of student scores
scores = np.array([85, 90, 75, 60, 95, 80, 70, 88])

# Searching for specific scores (e.g., 75 and 90) and returning their indices
score_to_find_1 = 75
score_to_find_2 = 90

indices_75 = np.where(scores == score_to_find_1)[0]  # Indices of score 75
indices_90 = np.where(scores == score_to_find_2)[0]  # Indices of score 90

print(f"Indices of score {score_to_find_1}: {indices_75}")
print(f"Indices of score {score_to_find_2}: {indices_90}")

# Sorting the array in ascending order
sorted_ascending = np.sort(scores)
print("Scores in ascending order :", sorted_ascending)

# Sorting the array in descending order
sorted_descending = np.sort(scores)[::-1]
print("Scores in descending order :", sorted_descending)