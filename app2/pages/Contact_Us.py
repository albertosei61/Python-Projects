import streamlit as st
from send_email import email_conn
import pandas as pd


df = pd.read_csv("topics.csv")
st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    for row in df:
        topic_choice = st.selectbox("What topic do you want to discuss?", df["topic"] )

    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}
{topic_choice}
From: {user_email}
{raw_message}
  
"""
    button = st.form_submit_button("Submit")
    if button:
       email_conn(message)
       st.info("Your email was sent succesfully!")