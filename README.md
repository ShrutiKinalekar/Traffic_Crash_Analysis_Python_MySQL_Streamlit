**Traffic Crash Analytics & Safety Intelligence Platform**

​This project focuses on leveraging SQL and data engineering techniques to extract actionable insights from a large-scale dataset of traffic crashes. By analyzing patterns, trends, and risk factors, this platform provides intelligence to support road safety initiatives, emergency response optimization, and urban planning decisions.

**​Project Overview**

​The objective of this project is to transform structured traffic crash data into meaningful business insights using advanced SQL querying and Python-Streamlit integration. The analysis covers various aspects, including high-risk locations, peak crash times, contributing causes, and environmental impact.

**​Key Features**

- ​**Database Management**: Data loading and exploration using MySQL.
- ​**Advanced SQL Analysis**: Implementation of complex queries, including:
  - ​Aggregations and Groupings.
  - ​Window Functions (e.g., ROW_NUMBER(), RANK(), LAG()).
  - ​Common Table Expressions (CTEs).
  - ​Joins and subqueries.

**Interactive Dashboard**: A Streamlit application that showcases SQL results in a clean, table-based format with corresponding business insights.

**​Dataset Information**

- - ​**Dataset Name**: Chicago Traffic Crashes
    - ​**Source**: Chicago Data Portal
    - ​**Volume**: 600,000+ records
    - ​**Time Range**: 2015 - Present

**​Project Structure**

**Data** : 

Traffic Data 

Crash_Queries_Analysis  #CSV file mapping Queries to Sql Command and Analysis

**Scripts**

ConnectDatabase.py # Script to connect to Database

CSVDataFrameUnderstanding # Script to analyse data

Crashes.py # Streamlit dashboard application

**SQL Queries**

Traffic_SQL_Queries.sql # All 15 Sql Queries.

requirements.txt # List of dependencies



**Business Impact**

​This platform enables stakeholders to:

​**Traffic Authorities:** Identify high-risk streets and accident-prone zones.

​**Insurance Companies:** Analyze factors contributing to high-severity crashes.

​**Emergency Services:** Evaluate response effectiveness using time-based data.

​**Urban Planning:** Understand the impact of road types and conditions.

​**Research & Policy Making:** Study crash trends and contributing causes.
