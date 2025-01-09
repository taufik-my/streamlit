import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25) # min, max, default
st.write('I’m ', age, ' years old.')

st.subheader('Range Slider')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))

st.write('Values:', values)

st.subheader('Time Slider')

appointment = st.slider('Schedule your appointment:', value=(time(11, 30), time(12, 45)))

st.write('You scheduled your appointment for:', appointment)

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30), # 2020-01-01 09:30
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)