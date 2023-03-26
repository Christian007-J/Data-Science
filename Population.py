import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv("D:\DATA CAMP\DATA\population.csv", index_col=0)
n = 2010
years = []
while n < 2020:
    n = n+1
    years.append(str(n))

uganda = population.loc[['UGA'], years]
print(uganda)
print(years)
print("My name is AINAMANI CHRISTIAN")
