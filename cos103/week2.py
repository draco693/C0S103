#question 1
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ")
temperature = float(input("Enter the temperature: "))

if choice == "1":
	converted_temperature = (temperature * 9 / 5) + 32
	print(f"{temperature}°C = {converted_temperature:.2f}°F")
elif choice == "2":
	converted_temperature = (temperature - 32) * 5 / 9
	print(f"{temperature}°F = {converted_temperature:.2f}°C")
else:
    print("Error: invalid choice.")

#question 2
student_name = "Amios"
age = 20
height = 1.75
is_student = True

print("Variable values and types:")
print(student_name, ":", type(student_name))
print(age, ":", type(age))
print(height, ":", type(height))
print(is_student, ":", type(is_student))

#question 3

print("Area Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

shape = input("Choose a shape (1-3): ")

if shape == "1":
	radius = float(input("Enter the radius: "))
	area = 3.14159 * radius ** 2
	print(f"Area of the circle: {area:.2f}")
elif shape == "2":
	length = float(input("Enter the length: "))
	width = float(input("Enter the width: "))
	area = length * width
	print(f"Area of the rectangle: {area:.2f}")
elif shape == "3":
	base = float(input("Enter the base: "))
	height_of_triangle = float(input("Enter the height: "))
	area = 0.5 * base * height_of_triangle
	print(f"Area of the triangle: {area:.2f}")
else:
	print("Error: invalid shape choice.")
