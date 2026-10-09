#question 1
number = float(input("Enter a number: "))

if number > 0:
	print("The number is positive.")
elif number < 0:
	print("The number is negative.")
else:
	print("The number is zero.")

#question 2
password = input("Enter a password: ")

if len(password) < 6:
	print("Password strength: Weak")
elif len(password) < 10:
	print("Password strength: Medium")
else:
	print("Password strength: Strong")

#question 3
score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
	print("Invalid score.")
elif score >= 70:
	print("Grade: A")
elif score >= 60:
	print("Grade: B")
elif score >= 50:
	print("Grade: C")
elif score >= 40:
	print("Grade: D")
else:
	print("Grade: F")


