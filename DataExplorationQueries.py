#Phase 2: Data Exploration
#  importing library
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import mysql.connector
from tabulate import tabulate

#Connecting to Database
DB_PASSWORD = "MySQL@1234"

connection = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD,database="Traffic")

#Creating cursor object
cursor = connection.cursor()


# Query to Count Total Rows in the Table
query = "SELECT COUNT(*) FROM trafficcrash;"
cursor.execute(query)
rows = cursor.fetchall()
print(tabulate(rows, headers=[i[0] for i in cursor.description]))

#Query to Describe Table Schema and DataTypes
query = "DESCRIBE trafficcrash;"
cursor.execute(query)
rows = cursor.fetchall()
print(tabulate(rows, headers=[i[0] for i in cursor.description]))
