import pandas as pd

netflix = pd.read_csv("D:/DATA CAMP/DATA/netflix_data.csv")

# Print the head of the homelessness data
print(netflix.head())

# Print information about homelessness
print(netflix.info())

# Print the shape of homelessness
print(netflix.shape)

# Print a description of homelessness
print(netflix.describe())

# Print the values of homelessness
print(netflix.values)

# Print the column index of homelessness
print(netflix.columns)

# Print the row index of homelessness
print(netflix.index)
