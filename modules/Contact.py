import streamlit as st

def kontak():
    st.title("Contact Me")
    st.write("I appreciate the opportunity to communicate in person and am also pleased to connect through the following links:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/fajrimughni/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/Fajrimughni)"
    )

    # Email
    st.write("📧 Email: fajriilhammughni@gmail.com")
