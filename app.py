import streamlit as st
import pandas as pd
import os 
from io import BytesIO

st.set_page_config(page_title="Data Sweeper",layout="wide")
st.title("Streamlit App")
st.write("First App Using Streamlit and Python")

upload_files = st.file_uploader("Upload Files ",type=["csv","xlsx"],accept_multiple_files=True)

if upload_files:
    for file in upload_files:
        file_ext=os.path.splitext(file.name)[-1].lower()
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext== ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error("Unsupported File Format!")
            continue


# DISPLAYING FILE INFO
    st.write(f"File Name : {file.name}")
    st.write(f"File Size : {file.size/1000000} mb")
    st.write("First 5 Rows")
    st.dataframe(df.head())