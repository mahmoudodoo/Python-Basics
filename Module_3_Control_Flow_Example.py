
# Module 3: Control Flow - Example Script

# Conditional Statements
print("Conditional Statements Example:")
age = 18
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are not old enough to vote.")

# Loops
# 'for' loop example
print("\n'for' Loop Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 'while' loop example
print("\n'while' Loop Example:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Nested loops and conditional statements
print("\nNested Loops and Conditional Statements Example:")
for x in range(1, 4):  # Outer loop
    for y in range(1, 3):  # Inner loop
        print(f"x = {x}, y = {y}", end='; ')
        # Conditional statement inside nested loop
        if x == y:
            print("x is equal to y")
        else:
            print("x is not equal to y")
