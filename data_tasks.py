
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. NumPy array and mean
array = np.arange(1, 11)
array_mean = np.mean(array)
print("NumPy Array:", array)
print("Mean of array:", array_mean)

# 2. Pandas DataFrame and summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 40],
    'Score': [88, 92, 85, 90]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# 3. API call (commented out due to no internet in some environments)
# import requests
# response = requests.get("https://api.agify.io/?name=michael")
# print("\nPredicted age for 'Michael':", response.json().get('age', 'No age found'))

# 4. Matplotlib line plot
x = np.arange(1, 11)
y = x ** 2
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title('Line Graph of y = x^2')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
plt.tight_layout()
plt.savefig("line_graph.png")  # Saves plot in current directory
print("\nLine graph saved as 'line_graph.png'")
