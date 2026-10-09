import numpy as np


# Practical exercise 1: create and manipulate NumPy arrays
def create_arrays():
	# NumPy arrays let us do calculations on many values at once.
	numbers = np.array([10, 20, 30, 40, 50])
	print("Array:", numbers)

	print("First value:", numbers[0])
	print("Values from index 1 to 3:", numbers[1:4])

	numbers[0] = 99
	print("After changing the first value:", numbers)


# Practical exercise 2: perform mathematical operations with NumPy arrays
def array_math():
	first_array = np.array([2, 4, 6])
	second_array = np.array([1, 3, 5])

	print("First array:", first_array)
	print("Second array:", second_array)
	print("Addition:", first_array + second_array)
	print("Subtraction:", first_array - second_array)
	print("Multiplication:", first_array * second_array)
	print("Division:", first_array / second_array)


# Practical exercise 3: multiply two matrices with NumPy
def matrix_multiplication():
	first_matrix = np.array([[1, 2], [3, 4]])
	second_matrix = np.array([[5, 6], [7, 8]])

	print("First matrix:")
	print(first_matrix)
	print("Second matrix:")
	print(second_matrix)
	print("Matrix multiplication:")
	print(first_matrix @ second_matrix)


# Run one exercise at a time by removing # from its function call.
# create_arrays()
# array_math()
#matrix_multiplication()
