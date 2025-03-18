import streamlit as st

def get_poem():
    return ("The Journey", "Mary Oliver", "One day you finally knew what you had to do...")

def display_poem():
    st.title("📜 Poem of the Day")
    try:
        poem_title, poet_name, poem_content = get_poem()
        st.header(poem_title)
        st.subheader(f"by {poet_name}")
        st.write(poem_content)
    except Exception as e:
        st.error(f"⚠️ Failed to fetch poem. Error: {e}")
    st.caption("Powered by Poemist API")
