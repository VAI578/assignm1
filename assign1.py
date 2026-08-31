
# Task 1: Perform Basic Mathematical Operations

# Taking two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Displaying results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

# Checking division by zero
if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero.")





# Task 2: Create a Personalized Greeting
# Task 2: Create a Personalized Greeting

# Step 1: Take user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 2: Concatenate names
full_name = first_name + " " + last_name

# Step 3: Print personalized greeting
print(f"Hello, {full_name}! Welcome to the Python program.")




