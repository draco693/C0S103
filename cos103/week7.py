# Practical exercise 1: square every number in a list
def square_numbers(numbers):
	"""Return a new list containing the square of each number."""
	return [number ** 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]
print("--- Squared Numbers ---")
print(square_numbers(numbers))


# Practical exercise 2: use lambda functions with map and filter
double = lambda number: number * 2
even_numbers = lambda number: number % 2 == 0

print("\n--- Lambda, Map, and Filter ---")
print(f"Doubled numbers: {list(map(double, numbers))}")
print(f"Even numbers: {list(filter(even_numbers, numbers))}")


# Practical exercise 3: sort dictionaries by a specified key
def sort_by_key(items, key):
	"""Return dictionaries sorted by the value of the specified key."""
	return sorted(items, key=lambda item: item[key])


students = [
	{"name": "Grace", "score": 88},
	{"name": "Alan", "score": 95},
	{"name": "Ada", "score": 91},
]

print("\n--- Sorted Dictionaries ---")
print(sort_by_key(students, "score"))
print(sort_by_key(students, "name"))
