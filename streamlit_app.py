import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My new app")
st.write(
    "Let's start hacking our project to help FBCs and the traditional network."
)
st.write("Hello, *World!* :sunglasses:")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
