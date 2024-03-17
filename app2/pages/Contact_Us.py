import streamlit as st

st.header("Contact Me")
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    email_submit = st.form_submit_button("Submit")
    print(email_submit)
    if email_submit:
        message = message + user_email
        print(email_submit)
        print("I was pressed")