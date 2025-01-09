import streamlit as st

st.header("Selectbox")

option = st.selectbox(
    'Which number do you like best?',
    ("1", "2", "3", "4", "5")
)

st.write('You selected:', option)

st.header("Multiselect")

options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'], # options
    ['Yellow', 'Red'] # default value
)

st.write('You selected:', options)