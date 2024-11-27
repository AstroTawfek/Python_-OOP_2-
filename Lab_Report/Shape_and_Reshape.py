"""
Scenario: You have a 1D array representing data from multiple sensors over a period. To
perform matrix operations, you need to restructure the data into a 2D format where each row
represents a sensor and each column represents a timestamp.

Question:
Given a 1D NumPy array, write code to:
● Reshape it into a 2D array with an appropriate number of rows and columns.
● If the reshaping is not possible due to mismatched elements, explain the error and provide
a solution by padding/truncating the data.
Demonstrate the reshaping and necessary checks on a sample array.

"""


import numpy as np

# Sample 1D array (sensor data)
sensor_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 9 elements

# Define the desired shape
num_sensors = 3  # Number of rows
num_timestamps = 3  # Number of columns

# Check if reshaping is possible
if sensor_data.size != num_sensors * num_timestamps:
    print(f"Reshaping not possible : {sensor_data.size} elements cannot form a {num_sensors}x{num_timestamps} array.")
    
    # Determine how to pad or truncate
    total_elements_needed = num_sensors * num_timestamps
    if sensor_data.size < total_elements_needed:
        # Need to pad the array
        padding_size = total_elements_needed - sensor_data.size
        padded_data = np.pad(sensor_data, (0, padding_size), 'constant', constant_values=0)
        reshaped_array = padded_data.reshape(num_sensors, num_timestamps)
        print("Padded and reshaped array :")
    else:
        # Need to truncate the array
        truncated_data = sensor_data[:total_elements_needed]
        reshaped_array = truncated_data.reshape(num_sensors, num_timestamps)
        print("Truncated and reshaped array :")
else:
    # Reshape the array directly
    reshaped_array = sensor_data.reshape(num_sensors, num_timestamps)
    print("Reshaped array :")

# Display the reshaped array
print(reshaped_array)