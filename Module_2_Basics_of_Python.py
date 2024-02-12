
# Module 2: Basics of Python - Example Script

# Variables and Data Types
x = 10  # Integer
y = 5.5  # Float
name = "Python Learner"  # String
is_programming_fun = True  # Boolean

# Print variables
print("Integer:", x)
print("Float:", y)
print("String:", name)
print("Boolean:", is_programming_fun)

# Basic Operators
sum = x + y  # Addition
difference = x - y  # Subtraction
product = x * y  # Multiplication
quotient = x / y  # Division

# Print the results of basic operations
print("\nBasic Operations:")
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Input and Output
# Uncomment the lines below to try out input and output
# user_name = input("Enter your name: ")
# print("Hello, " + user_name + "! Welcome to Python.")

# String Manipulation
greeting = "Hello"
user_name = "Alice"
message = f"{greeting}, {user_name}!"
print("\nString Manipulation:")
print(message)

# Basic Error Handling
try:
    # Attempt to convert input to an integer
    # For the purpose of this example, we'll simulate user input
    user_input = "not a number"  # Simulate user input
    number = int(user_input)
except ValueError:
    print("\nError Handling:")
    print("That was not a valid number. Please enter an integer.")
