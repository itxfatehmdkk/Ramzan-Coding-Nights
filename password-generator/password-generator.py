import streamlit as st
import random
import string 


def generate_password(length,use_digits,use_special):
    characters = string.ascii_letters    # ascii  method of string module provide us upper-case and lower-case letters.

    if use_digits:
        characters += string.digits      # digits method provide numbers (0-9)

    if use_special:
        characters += string.punctuation  # punction method provide pecial characters(!, @, #, $, %, ^, &, *, (), _, +)

    return "".join(random.choice(characters) for _ in range(length)) 

st.title("Password Generator")

length = st.slider(" Select Password Length", min_value=6, max_value=30, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length,use_digits,use_special)
    st.write(f"Generated Password: `{password}`")

st.write("------------------------")

st.write("Build with ❤️ by [Fateh Muhammad Durrani](https://github.com/itxfatehmdkk)")
