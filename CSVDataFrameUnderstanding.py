#Phase 1: Data Loading & Understanding

#  importing libraries
import warnings
warnings.filterwarnings('ignore')


from tabulate import tabulate

import pandas as pd
import mysql.connector

# Creating Dataframe to read CSV

url = 'D:/Shruti/Guvi/Traffic Project/Python/Data/Traffic_CrashesData.csv'
df = pd.read_csv(url)

#Understanding the Data 

print("Data Types : ")
print(df.dtypes)

print("Total Rows and Columns : ")
print(df.shape)


print("Column Information : ")
print(df.info())

print("Table Records : ")
print(df.head)
