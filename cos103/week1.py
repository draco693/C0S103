#question 1
print("Amigos! I am practicing Python programming")

#question 2
print('Addition:', 8 + 3)
print('Subtraction:', 8 - 3)
print('Multiplication:', 8 * 3)
print('Division:', 8 / 3)
print('Floor division:', 8 // 3)
print('Remainder:', 8 % 3)
print('Power:', 8 ** 3)

#question 3
first_number = float(input("Enter the first number: "))
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operator = input("Enter your choice (1-4): ")
second_number = float(input("Enter the second number: "))
result = None

if operator == "1":
	result = first_number + second_number
elif operator == "2":
	result = first_number - second_number
elif operator == "3":
	result = first_number * second_number
elif operator == "4":
	if second_number == 0:
		print("Error: cannot divide by zero.")
	else:
		result = first_number / second_number
else:
	print("Error: invalid choice.")

if result is not None:
	print(f"Result: {result:.2f}")
