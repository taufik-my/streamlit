import streamlit as st
import time

st.title('Progress Bar')

with st.expander('About this app'):
    st.write('You can now display the progress of the calculations in a Streamlit app.')

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

st.balloons()