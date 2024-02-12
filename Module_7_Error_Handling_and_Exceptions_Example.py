
# Module 7: Error Handling and Exceptions - Example Script

# Try and Except Blocks
try:
    # This will raise an error because x is not defined
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Using else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally Block
try:
    print("Try something")
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Raising Exceptions
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
