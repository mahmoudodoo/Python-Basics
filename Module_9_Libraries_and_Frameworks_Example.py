
# Module 9: Libraries and Frameworks - Example Script

# NumPy Example
import numpy as np
arr = np.array([1, 2, 3])
print('NumPy Array:', arr)

# Pandas Example
import pandas as pd
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
print('\nPandas DataFrame:\n', df)

# Matplotlib Example
# Note: This code needs to be run in an environment that can display graphics.
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Matplotlib Example')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

# Flask Example
# Note: This is a basic example. To run a Flask application, you would need to save this in a file and run it with Flask.
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# 
# if __name__ == '__main__':
#     app.run(debug=True)
