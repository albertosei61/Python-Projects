import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")
st.write("Company ethics and way of life that aligns with employees lifestyle. Make it that every employee is fairly compensated\
          and also has a work life balance. This is achieved by having unlimited pto.")
st.subheader("Our Team")
col1, col2, col3 = st.columns(3, gap="large")
df = pd.read_csv("data.csv", sep=",")
print(df)

with col1:
    for index, row in df[:4].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        names = st.subheader(first_name + " " + last_name)
        st.caption(row["role"])
        st.image("images/" +row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        names = st.subheader(first_name + " " + last_name)
        st.caption(row["role"])
        st.image("images/" +row['image'])

with col3:
    for index, row in df[8:].iterrows():
        first_name = row["first name"].title()
        last_name = row["last name"].title()
        names = st.subheader(first_name + " " + last_name)

        st.caption(row["role"])
        st.image("images/" +row['image'])
