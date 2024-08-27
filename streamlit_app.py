import streamlit as st
import pandas as pd
import numpy as np
from st_files_connection import FilesConnection

st.title("🎈 My new app")
st.write(
    "Let's start hacking our project to help FBCs and the traditional network."
)
st.write("Hello, *World!* :sunglasses:")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
conn = st.connection('s3', type=FilesConnection)
df = conn.read("h4-hack-week-aug-2024/myfile.csv", input_format="csv", ttl=600)

for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
