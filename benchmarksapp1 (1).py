import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(
    page_title="CSV Data Viewer",
    layout="centered"
)

st.title("CSV Data Viewer from GitHub")

# GitHub Raw File URLs
fact_url = "https://raw.githubusercontent.com/nish1057/App1/refs/heads/main/Streamlit_Test_FactTable.csv"
dimension_url = "https://raw.githubusercontent.com/nish1057/App1/refs/heads/main/Streamlit_Test_DimTable.csv"

try:
    # Read CSV files from GitHub
    fact_df = pd.read_csv(fact_url)
    dimension_df = pd.read_csv(dimension_url)

    # Display Data
    st.write("### Fact Table")
    st.dataframe(fact_df)
    
    st.write("### Dimension Table")
    st.dataframe(dimension_df)
    
    # Merge tables on Responsible_ID
    merged_df = fact_df.merge(dimension_df, left_on='Responsible_ID', right_on='Responsible ID', how='inner')
    
    st.write("### Merged Data")
    st.dataframe(merged_df)

except Exception as e:
    st.error(f"Error loading data: {e}")
