import csv


PRACTICE_CSV_FILE = "practice.csv"
STUDENT_FILE = "students.csv"


# Practical exercise 1: count words, lines, and characters in a text file
def count_text_file():
	filename = input("Enter the name of the text file: ")

	try:
		with open(filename, "r") as file:
			text = file.read()
	except FileNotFoundError:
		print("That file was not found.")
		return

	words = text.split()
	lines = text.split("\n")

	print(f"Words: {len(words)}")
	print(f"Lines: {len(lines)}")
	print(f"Characters: {len(text)}")


# Practical exercise 2: write rows to a CSV file and read them back
def practice_csv():
	with open(PRACTICE_CSV_FILE, "w", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["Name", "Score"])
		while True:
			name = input("Enter a name (or press Enter to finish): ")
			if name == "":
				break
			score = input("Enter the score: ")
			writer.writerow([name, score])

	print(f"Wrote data to {PRACTICE_CSV_FILE}:")
	with open(PRACTICE_CSV_FILE, "r", newline="") as file:
		reader = csv.reader(file)
		for row in reader:
			print("\t".join(row))


# Practical exercise 3: manage student records stored in a CSV file
def add_student():
	student_id = input("Enter student ID: ")
	name = input("Enter student name: ")
	course = input("Enter course: ")

	try:
		with open(STUDENT_FILE, "r", newline="") as file:
			first_row = next(csv.reader(file), None)
	except FileNotFoundError:
		first_row = None

	if first_row is None:
		with open(STUDENT_FILE, "w", newline="") as file:
			writer = csv.writer(file)
			writer.writerow(["ID", "Name", "Course"])

	with open(STUDENT_FILE, "a", newline="") as file:
		writer = csv.writer(file)
		writer.writerow([student_id, name, course])
	print("Student added.")


def view_students():
	try:
		with open(STUDENT_FILE, "r", newline="") as file:
			reader = csv.reader(file)
			next(reader, None)
			found_student = False

			for row in reader:
				if row:
					print(f"ID: {row[0]}, Name: {row[1]}, Course: {row[2]}")
					found_student = True

			if not found_student:
				print("There are no student records.")
	except FileNotFoundError:
		print("No student records file exists yet.")


def delete_student():
	student_id = input("Enter the ID of the student to delete: ")
	try:
		with open(STUDENT_FILE, "r", newline="") as file: rows = list(csv.reader(file))
	except FileNotFoundError:
		print("No student records file exists yet."); return
	if len(rows) < 2: print("There are no student records."); return
	remaining_rows = [row for row in rows[1:] if row and row[0] != student_id]
	if len(remaining_rows) == len(rows[1:]): print("Student ID not found."); return
	with open(STUDENT_FILE, "w", newline="") as file:
		writer = csv.writer(file); writer.writerow(rows[0]); writer.writerows(remaining_rows)
	print("Student deleted.")


def student_database():
	while True:
		print("\n--- Student Database ---")
		print("1. Add student")
		print("2. View students")
		print("3. Delete student")
		print("4. Exit student database")
		choice = input("Choose an option: ")

		if choice == "1":
			add_student()
		elif choice == "2":
			view_students()
		elif choice == "3":
			delete_student()
		elif choice == "4":
			break
		else:
			print("Please choose 1, 2, 3, or 4.")


# Run one exercise at a time by removing # from its function call.
# count_text_file()
# practice_csv()
# student_database()
