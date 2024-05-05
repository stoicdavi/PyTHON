# working with mixed data types
import numpy as np
file = 'titanic.csv'
d = np.recfromcsv(file)
print(d[:3])