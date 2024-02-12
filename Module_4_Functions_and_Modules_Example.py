
# Module 4: Functions and Modules - Example Script

# Example of defining a function
def greet(name):
    '''Greet someone by their name.'''
    print(f"Hello, {name}!")

# Using the function
greet("Alice")

# Example of using function arguments and return values
def add_numbers(a, b):
    '''Return the sum of two numbers.'''
    return a + b

# Using the function
result = add_numbers(5, 3)
print("The sum is:", result)

# Example of importing and using a module
# Assuming 'mymodule.py' exists and has a function called 'say_hello'
# import mymodule
# mymodule.say_hello()

# Demonstrating a simple module with a function
def simple_module_func():
    print("This is a simple function inside a module-like script.")

# Calling the function within the same script
simple_module_func()

# Note: For real module usage, the module should be in a separate file and imported as shown in the commented code above.
