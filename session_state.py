import streamlit as st

st.title('Session State Example')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')

col1, spacer, col2 = st.columns([2,1,2])

with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

st.title('Weight Converter')

def lbs_to_kg(lbs):
    return lbs / 2.2046

def kg_to_lbs(kg):
    return kg * 2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:")
    kilogram = lbs_to_kg(pounds)
with col2:
    kilogram = st.number_input("Kilograms:")
    pounds = kg_to_lbs(kilogram)

st.header('Output')
st.write(f"Pounds: {pounds}, Kilograms: {kilogram}")