import numpy as np
import matplotlib.pyplot as plt
file = 'seaslug.txt'
# Load the data as strings
data = np.loadtxt(file, delimiter='\t', skiprows=1, dtype=str)
print(data[0])
# Load the data as floats
data_float = np.loadtxt(file, delimiter='\t', skiprows=1, dtype=float)
print(data_float[9])
#plot the scatter plot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()