import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Set up page configuration
st.set_page_config(
    page_title="Database Connection Test",
    layout="centered"
)

# Database connection
@st.cache_resource
def get_database_connection():
    server = 'db-pd-segmentprojects.database.windows.net'
    database = 'sqldb-pd-segmentprojects-pv-im'
    username = 'sa-segment-projects-pv-im-vba'
    password = 'gyggyf-vigket-4byJre'
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+18+for+SQL+Server'
    engine = create_engine(connection_string)
    return engine

# Main Application
st.title("Database Connection and Data Display")

# Connect to database
try:
    engine = get_database_connection()
    st.success("Connected to the database successfully!")

    # Query fact and dimension tables
    fact_query = "SELECT * FROM fact_table"
    dimension_query = "SELECT * FROM dimension_table"

    fact_df = pd.read_sql(fact_query, engine)
    dimension_df = pd.read_sql(dimension_query, engine)

    # Display data
    st.write("### Fact Table")
    st.dataframe(fact_df)

    st.write("### Dimension Table")
    st.dataframe(dimension_df)

except Exception as e:
    st.error(f"Error connecting to the database: {e}")
