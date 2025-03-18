import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters #provide uppercase and lowercase letters
    if use_digits:
        characters +=  string.digits #add digits

    if use_special_chars:
        characters += string.punctuation #add special characters
    return ''.join(random.choice(characters)for _ in range(length))

st.title("Password Generator")
length = st.slider("Password length", min_value= 8, max_value= 32, value= 12)
use_digits = st.checkbox("Include digits")
use_special_chars = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.success(f"Generated Password: `{password}`")

st.write("---")
st.write("Made by Kamran ali")
    
