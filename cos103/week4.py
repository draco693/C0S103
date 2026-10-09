#question 1
text = input("Enter a word or phrase: ")
clean_text = text.lower().replace(" ", "")
reversed_text = clean_text[::-1]

print(f"Original text: {text}")
print(f"Reversed text: {reversed_text}")

if clean_text == reversed_text:
	print("This is a palindrome.")
else:
	print("This is not a palindrome.")

#question 2
sample_text = " Python Programming is Fun! "

print(f"\nOriginal: '{sample_text}'")
print(f"Uppercase: {sample_text.upper()}")
print(f"Lowercase: {sample_text.lower()}")
print(f"Without extra spaces: '{sample_text.strip()}'")
print(f"Replace Python: {sample_text.replace('Python', 'String')}")
print(f"Starts with spaces: {sample_text.startswith(' ')}")
print(f"Ends with spaces: {sample_text.endswith(' ')}")
print(f"First character: {sample_text[1]}")
print(f"First word: {sample_text[1:7]}")

#question 3
print("\n--- Hangman ---")
secret_word = "python"
guessed_letters = ""
attempts = 6

while attempts > 0:
	masked_word = ""
	for letter in secret_word:
		if letter in guessed_letters:
			masked_word += letter
		else:
			masked_word += "_"

	print(f"\nWord: {masked_word}")
	print(f"Attempts left: {attempts}")

	if "_" not in masked_word:
		print("You win!")
		break

	guess = input("Guess a letter: ").lower()

	if len(guess) != 1:
		print("Please enter one letter.")
	elif guess in guessed_letters:
		print("You already guessed that letter.")
	else:
		guessed_letters += guess
		if guess in secret_word:
			print("Correct!")
		else:
			attempts -= 1
			print("Incorrect.")
else:
	print(f"You lose! The word was '{secret_word}'.")
