import streamlit as st
import pandas as pd
import numpy as np

st.header('Line Chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 20 rows, 3 columns
    columns=['a', 'b', 'c'] # column names
)

st.line_chart(chart_data)

