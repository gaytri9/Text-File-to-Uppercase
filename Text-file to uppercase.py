import streamlit as st
import pandas as pd


def convert_file_to_uppercase(file_content):
    upper_content = file_content.upper()
    return upper_content

# Title
st.title('Convert Text File To UpperCase')

# File upload
file = st.file_uploader("Upload a text File", type="txt")

# Email input
email = st.text_input("Email Id")

# Submit button
if st.button("Submit"):
    if file is not None and email:
        # Read the text file
        text = file.read().decode("utf-8")

        # Convert the content to upper case
        upper_text = convert_file_to_uppercase(text)

        # Display the upper case content
        st.text_area("converted Text",upper_text,height=300)

        # Provide a download link for the converted text
        st.download_button(
            label="Download UpperCase Text",
            data=upper_text,
            file_name="uppercase_text.txt",
        )
    else:
        st.error("Please upload a file and enter a valid email address.")

if __name__ == "__main__":

    pass