
# Module 8: File Handling - Example Script

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, Python!')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Working with file paths
import os
file_path = os.path.join('folder', 'example.txt')
print(f'File path: {file_path}')

# Error handling in file operations
try:
    with open('nonexistentfile.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File does not exist')
