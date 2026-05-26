# Traffic Streamlit USER Interface

#--------------------------------- Import Liabraries-------------------------------------------
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import mysql.connector
from tabulate import tabulate
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


#------------------------------- Adding Gradient Background--------------------------------

gradient_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(90deg, #e3ffe7 0%, #d9e7ff 100%);
    background-size: cover;
}
</style>
"""

st.markdown(gradient_css, unsafe_allow_html=True)

sidebar_gradient_css = """
<style>
[data-testid="stSidebar"] {
    background-image: linear-gradient(90deg, #e3ffe7 0%, #d9e7ff 100%);
    background-size: cover;
}
"""
st.markdown(sidebar_gradient_css, unsafe_allow_html=True)

#------------------------------------Connecting to Database----------------------------------

DB_PASSWORD = "MySQL@1234"

conn = mysql.connector.connect(host="localhost",user="root",password=DB_PASSWORD,database="Traffic")

# Function to connect to MySql database
def get_data(query, params=None):
    
    if params:
        df = pd.read_sql_query(query, conn, params=params)
    else:
        df = pd.read_sql_query(query, conn)
    conn.close()
    return df

#--------------------Reading SQL Queries and Corresponding Analysis from CSV file
# Read Queries from CSV
url = 'D:/Shruti/Guvi/Traffic Project/Python/Data/Crash_Queries_Analysis.csv'

# file_id = '1hiz933qtMOlkF5pFoWh9GqaH4cVzo2s_'
# url = f'https://google.co{file_id}&export=download'

#st.write(url)

df = pd.read_csv(url)


#----------------------------------- Streamlit Layout-----------------------------------------

# Streamlit App Title
st.set_page_config(page_title="Traffic Crash Analytics", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation : ")
page = st.sidebar.radio("Go To", ["Project Introduction", "Crash Data Visualization", "Crash Data Analysis",
                                   "Creator Information"])

#-----------------------------Project Introduction Page ----------------------------------------

if page == "Project Introduction":
    st.title("Traffic Crash Analytics & Safety Intelligence Platform")
    st.image("D:/Shruti/Guvi/Traffic Project/Python/Data/traffic.jpg")
    st.subheader("📊 Welcome to the Traffic Crash Analytics & Safety Intelligence Platform")
    st.write("""A comprehensive analytical tool designed to transform large-scale traffic data into 
              actionable road safety insights. By leveraging advanced SQL techniques, this platform 
              empowers users to uncover critical patterns, identify high-risk zones, and evaluate 
              environmental impact on crash severity. Whether you are a traffic authority, urban planner,
               or policy researcher, our application provides the data-driven intelligence needed to 
              optimize emergency responses and support life-saving infrastructure decisions..""")
              
#----------------------------Crash Data Visualization page-------------------------------------

elif page == "Crash Data Visualization":
    st.title("Crash Data Visualizer")
    st.write("""The Charts & Visualizations page acts as the operational nerve center of the application,
              transforming raw, complex data streams into immediate, actionable intelligence. Designed 
             for maximum cognitive clarity, it features a fluid grid of interactive bar charts, granular
              time-series line graphs, and categorical breakdown rings that let users monitor performance 
             metrics at a glance.""")
    
# Checkbox to select Chart type

    st.subheader('Chart Type')
    chart_type1 = st.checkbox('Line Chart')
    chart_type2 = st.checkbox('Bar Chart')
    chart_type3 = st.checkbox('Area Chart')

    x_column = st.selectbox('Chart based on :',['PRIM_CONTRIBUTORY_CAUSE','SEC_CONTRIBUTORY_CAUSE','CRASH_MONTH','year'])

# Column layout to display Multiple Charts
    col1,col2,col3 = st.columns(3,gap='small')

    chart_query = f"SELECT {x_column},count(*) AS Total_Crashes FROM trafficcrash GROUP BY {x_column};"
    
    chart_df = pd.read_sql_query(chart_query, conn)
    
    
    if chart_type1 :
        with col1:
            col1.title("Line Chart")
            st.line_chart(chart_df,x=x_column,y="Total_Crashes")
    if chart_type2:
        with col2:
            col2.title("Bar Chart")
            st.bar_chart(chart_df,x=x_column,y="Total_Crashes")
    if chart_type3 :
        with col3:
            col3.title("Area Chart")
            st.area_chart(chart_df,x=x_column,y="Total_Crashes")



#---------------------- Crash Data Analysis -SQl Query page --------------------------------------

elif page == "Crash Data Analysis":
    st.header("Crash Data Analysis")
    st.write("""The Query page serves as the precision engine of the application, empowering users
              to extract specific, granular information from massive information repositories with absolute
              speed.""")
    st.subheader("Business Usecases")
    usecase = ['Traffic Authorities','Insurance Companies','Emergency Services','Urban Planning','Research & Policy Making']


# Radio buttons to select usecase

    selected_usecase = st.radio("**Choose a Business CASE**",usecase)

    if selected_usecase == "Traffic Authorities":
        st.write("__Usecase Objective__ : Identify high-risk streets and accident-prone zones")
        df_filtered = df[df['USECASE'] == "Traffic"]


# Selectbox to select Query for business insight.
# Using Dataframe to fetch SQL queries and correspnding Analysis from CSV file
        
        column_name = df_filtered["Query"]
        selected_query = st.selectbox("**Choose a Query**",column_name)
        st.subheader("Business insight")
        df_filtered_query = df_filtered[df_filtered["Query"] == selected_query]
        
        df_filtered_analysis = (df_filtered_query["ANALYSIS"].tolist())
        df_filtered_sql = (df_filtered_query["SQL_Query"].tolist())
        st.write(df_filtered_analysis[0])
        
        query_result = get_data(str(df_filtered_sql[0]))
    elif selected_usecase == "Insurance Companies":
        st.write("__Usecase Objective__ : Analyze factors contributing to high-severity crashes")
        df_filtered = df[df['USECASE'] == "INSURANCE"]

        column_name = df_filtered["Query"]
        selected_query = st.selectbox("**Choose a Query**",column_name)
        st.subheader("Business insight")
        df_filtered_query = df_filtered[df_filtered["Query"] == selected_query]
        
        df_filtered_analysis = (df_filtered_query["ANALYSIS"].tolist())
        df_filtered_sql = (df_filtered_query["SQL_Query"].tolist())
        st.write(df_filtered_analysis[0])
        
        query_result = get_data(str(df_filtered_sql[0]))
    elif selected_usecase == "Emergency Services":
        st.write("__Usecase Objective__ : Evaluate response effectiveness using time-based data")
        df_filtered = df[df['USECASE'] == "Emergency"]

        column_name = df_filtered["Query"]
        selected_query = st.selectbox("**Choose a Query**",column_name)
        st.subheader("Business insight")
        df_filtered_query = df_filtered[df_filtered["Query"] == selected_query]
        
        df_filtered_analysis = (df_filtered_query["ANALYSIS"].tolist())
        df_filtered_sql = (df_filtered_query["SQL_Query"].tolist())
        st.write(df_filtered_analysis[0])
        
        query_result = get_data(str(df_filtered_sql[0]))   
    
    elif selected_usecase == "Urban Planning":
        st.write("__Usecase Objective__ : Understand impact of road types and conditions")
        df_filtered = df[df['USECASE'] == "URBAN"]

        column_name = df_filtered["Query"]
        selected_query = st.selectbox("**Choose a Query**",column_name)
        st.subheader("Business insight")
        df_filtered_query = df_filtered[df_filtered["Query"] == selected_query]
        
        df_filtered_analysis = (df_filtered_query["ANALYSIS"].tolist())
        df_filtered_sql = (df_filtered_query["SQL_Query"].tolist())
        st.write(df_filtered_analysis[0])
        
        query_result = get_data(str(df_filtered_sql[0])) 

    elif selected_usecase == "Research & Policy Making":
        st.write("__Usecase Objective__ : Study crash trends and contributing causes")
        df_filtered = df[df['USECASE'] == "Research"]

        column_name = df_filtered["Query"]
        selected_query = st.selectbox("**Choose a Query**",column_name)
        st.subheader("Business insight")
        df_filtered_query = df_filtered[df_filtered["Query"] == selected_query]
        
        df_filtered_analysis = (df_filtered_query["ANALYSIS"].tolist())
        df_filtered_sql = (df_filtered_query["SQL_Query"].tolist())
        st.write(df_filtered_analysis[0])
        
        query_result = get_data(str(df_filtered_sql[0])) 

    st.write("### Query Result:")
    st.dataframe(query_result,hide_index=True)

#--------------------------Creator Infromation Page--------------------------------

elif page == "Creator Information":
    st.title("Creator Information")
    st.subheader("Name : Shruti Kinalekar")
    st.write("""Software Engineer with total 8 years of experience in Software Testing.
             \nCurrently working on Data Science Projects.
             \nTools : Python, MySQl, Streamlit,vc++,Oracle""")
    


#--------------------------------------------END---------------------------------------------