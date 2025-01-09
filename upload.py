import streamlit as st
import pandas as pd

st.header("File Upload")

st.subheader("Input file")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df)
    st.subheader("Dataframe Summary")
    st.write(df.describe())
else:
    st.info("Awaiting for CSV file to be uploaded.")