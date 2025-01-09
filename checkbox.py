import streamlit as st

st.header("Checkbox")

st.write('What would you like to order?')

icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write('You ordered Ice Cream')
if coffee:
    st.write('You ordered Coffee')
if cola:
    st.write('You ordered Cola')
