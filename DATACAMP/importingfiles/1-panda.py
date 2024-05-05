import pandas as pd
file = 'digits.csv'
data = pd.read_csv(file, nrows=5, header=None)
print(data.head())
# build a numpy array from the DataFrame:
data_array = data.values
print(type(data_array))