#Phase 1: Data Loading to MySql 

#  importing libraries
import warnings
warnings.filterwarnings('ignore')

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse

from tabulate import tabulate

import pandas as pd
import mysql.connector

# Database credentials 
DB_USER = "root"
DB_PASSWORD = "MySQL@1234"
DB_HOST = "localhost"       # or IP address
DB_PORT = 3306              # default MySQL port
DB_NAME = "traffic"


#Connecting to MySQL

connection = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD)
#Creating cursor object
cursor = connection.cursor()


# Create Database

query = ("CREATE DATABASE IF NOT EXISTS TRAFFIC;")
cursor.execute(query)


# Safely encode password in case it contains special characters
encoded_password = urllib.parse.quote_plus(DB_PASSWORD)

# Create the connection URL
connection_url = f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(connection_url, echo=True, pool_pre_ping=True)

# Test the connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT VERSION()"))
    version = result.scalar()
    print(f"Connected to MySQL Server version: {version}")


# Creating Dataframe to read CSV

url = 'D:/Shruti/Guvi/Traffic Project/Python/Data/Traffic_CrashesData.csv'
df = pd.read_csv(url)


#Transferring Data From CSV to MySQL Table
df.to_sql(name="trafficcrash",con=engine,if_exists='replace',chunksize=5000,method="multi",index=False)

