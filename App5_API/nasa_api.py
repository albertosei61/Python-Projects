import streamlit as st
import requests

page = st.set_page_config(page_title="Nasa Astronomy", layout="centered")

api_key = "H99GduA3SZmTNKtfzRg0WHivjDRpfbEEfD5L4JjA"
url = "https://api.nasa.gov/planetary/apod?api_key=H99GduA3SZmTNKtfzRg0WHivjDRpfbEEfD5L4JjA"

response = requests.get(url)
data = response.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response1 = requests.get(image_url)
with open(image_filepath, "wb") as file:
        file.write(response1.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)