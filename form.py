import streamlit as st

st.title('Form')

st.header('1. Example of using `with` notation')

st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('Select your coffee:')

    coffee_beans = st.selectbox('Coffee beans:', ['Arabica', 'Robusta'])
    coffee_roast = st.selectbox('Coffee roast:', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method:', ['Espresso', 'Pour-over', 'French press'])
    serving_type = st.selectbox('Serving type:', ['Cup', 'Mug', 'Takeaway'])
    milk_val = st.select_slider('Milk:', options=['No milk', 'Splash', 'Half', 'Full'])
    owncup_val = st.checkbox('Bring your own cup')

    submitted = st.form_submit_button('Brew coffee')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_beans}`
        - Coffee roast: `{coffee_roast}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)