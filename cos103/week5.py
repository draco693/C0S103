#question 1 - Contact book using a dictionary
contact_book = {}

while True:
	print("\n--- Contact Book ---")
	print("1. Add or update a contact")
	print("2. Look up a contact")
	print("3. View all contacts")
	print("4. Delete a contact")
	print("5. Exit contact book")
	choice = input("Choose an option: ")

	if choice == "1":
		name = input("Enter the contact name: ").strip()
		phone = input("Enter the phone number: ").strip()
		contact_book[name] = phone
		print("Contact saved.")
	elif choice == "2":
		name = input("Enter the name to look up: ").strip()
		if name in contact_book:
			phone = contact_book[name]
			print(f"{name}: {phone}")
		else:
			print("Contact not found.")
	elif choice == "3":
		if contact_book:
			for name, phone in contact_book.items():
				print(f"{name}: {phone}")
		else:
			print("The contact book is empty.")
	elif choice == "4":
		name = input("Enter the name to delete: ").strip()
		if name in contact_book:
			del contact_book[name]
			print("Contact deleted.")
		else:
			print("Contact not found.")
	elif choice == "5":
		break
	else:
		print("Please choose an option from 1 to 5.")


#question 2 - List and set operations
numbers = [8, 3, 5, 3, 1]
print("\n--- List Operations ---")
print(f"Original list: {numbers}")
print(f"First item: {numbers[0]}")
print(f"Items from index 1 to 3: {numbers[1:4]}")

numbers.append(10)
numbers.extend([12, 15])
numbers.insert(1, 7)
print(f"After append, extend, and insert: {numbers}")
print(f"Number of 3s: {numbers.count(3)}")
print(f"Index of the first 3: {numbers.index(3)}")
popped_number = numbers.pop()
print(f"Popped item: {popped_number}")
numbers.remove(3)
numbers.sort()
print(f"After remove and sort: {numbers}")
numbers.reverse()
print(f"After reverse: {numbers}")

student_record = ("Sam", 85)
print(f"\nTuple record: {student_record}")
print("Tuples are immutable, so their items cannot be changed after creation.")

first_group = {1, 2, 3, 4}
second_group = {3, 4, 5, 6}
small_group = {3, 4}
print("\n--- Set Operations ---")
print(f"First set: {first_group}")
print(f"Union: {first_group | second_group}")
print(f"Intersection: {first_group & second_group}")
print(f"Difference: {first_group - second_group}")
print(f"Is small_group a subset of first_group? {small_group.issubset(first_group)}")
print(f"Is first_group a superset of small_group? {first_group.issuperset(small_group)}")


#question 3 - Student scores
students = []
scores = []
student_count = int(input("\nHow many students? "))

for number in range(student_count):
	name = input(f"Enter the name of student {number + 1}: ").strip()
	score = float(input(f"Enter {name}'s score: "))
	students.append((name, score))
	scores.append(score)

if students:
	total_score = 0
	highest_score = max(scores)
	highest_scoring_students = []
	for name, score in students:
		total_score += score
		if score == highest_score:
			highest_scoring_students.append(name)
	average_score = total_score / len(students)
	students.sort(key=lambda student: student[0].lower())

	print(f"\nHighest score: {highest_score}")
	print(f"Student(s) with the highest score: {', '.join(highest_scoring_students)}")
	print(f"Average score: {average_score:.2f}")
	print("Students in alphabetical order:")
	for name, score in students:
		print(f"{name}: {score}")
else:
	print("No student scores were entered.")
