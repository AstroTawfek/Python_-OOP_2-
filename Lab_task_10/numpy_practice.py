import numpy as np
numbers = np.array([2.5,3.9,5.2,7.3,11.7])
print(numbers)
print(type(numbers))
newer = numbers.astype(int)
print(newer.dtype)

array_id = np.array([[2,3,4,5,6], [2,3,4,5,6], [2,3,4,5,6]])
print(type(array_id))
print()

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)