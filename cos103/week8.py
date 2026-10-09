# Practical exercise 1: calculate a factorial recursively
def factorial(number):
	if number == 0 or number == 1:
		return 1
	return number * factorial(number - 1)


print("--- Recursive Factorial ---")
print(f"5! = {factorial(5)}")


# Practical exercise 2: use a decorator to log function calls
def log_calls(function):
	def wrapper(*args, **kwargs):
		print(f"Calling {function.__name__}")
		result = function(*args, **kwargs)
		print(f"Finished {function.__name__}")
		return result

	return wrapper


@log_calls
def multiply(first_number, second_number=1):
	return first_number * second_number


print("\n--- Decorator ---")
print(multiply(4, second_number=3))


# Practical exercise 3: solve the Tower of Hanoi recursively
def tower_of_hanoi(disks, source="A", auxiliary="B", target="C"):
	if disks == 1:
		print(f"Move disk 1 from {source} to {target}")
		return

	tower_of_hanoi(disks - 1, source, target, auxiliary)
	print(f"Move disk {disks} from {source} to {target}")
	tower_of_hanoi(disks - 1, auxiliary, source, target)


print("\n--- Tower of Hanoi ---")
tower_of_hanoi(3, source="A", auxiliary="B", target="C")
