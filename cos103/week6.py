import random


# Question 1 - Prime numbers up to a given number
print("\n--- Prime Numbers ---")
limit = int(input("Print prime numbers up to: "))
print(f"Prime numbers up to {limit}:")

for candidate in range(2, limit + 1):
	is_prime = True
	for divisor in range(2, candidate):
		if candidate % divisor == 0:
			is_prime = False
			break
	if is_prime:
		print(candidate)


# Question 2 - Multiplication table using nested loops
print("\n--- Multiplication Table ---")
table_size = int(input("Enter the table size: "))

for row in range(1, table_size + 1):
	for column in range(1, table_size + 1):
		print(row * column, end=" ")
	print()


# Question 3 - Number guessing game
print("\n--- Number Guessing Game ---")
secret_number = random.randint(1, 100)
guess_count = 0

while True:
	guess = int(input("Guess a number from 1 to 100: "))
	if guess < 1 or guess > 100:
		print("Please enter a number from 1 to 100.")
		continue

	guess_count += 1

	if guess < secret_number:
		print("Too low. Try again.")
	elif guess > secret_number:
		print("Too high. Try again.")
	else:
		print(f"Correct! You guessed it in {guess_count} tries.")
		break
