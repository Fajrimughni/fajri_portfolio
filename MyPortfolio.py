import streamlit as st

# Konfigurasi halaman harus paling atas
st.set_page_config(layout='wide')

import modules.About as about
import modules.Contact as contact
import modules.Project as project
import modules.Poem as poem
import modules.Background as background
import modules.Music as music

# Judul & Header
st.title("Fajri's Portfolio")
st.header("Jakarta Based Database Geologist and Data Scientist")

# Sidebar Navigasi
st.sidebar.title("Navigation")
page = st.sidebar.radio("Please Decide:", ['About Me', 'Contact', 'Project A', 'Project B', 'Poem'])

# **Navigasi ke Halaman yang Dipilih**
if page == 'About Me':
    about.about_me()
elif page == 'Contact':
    contact.kontak()
elif page == 'Project A':
    project.display_project_a()  # Memanggil Project A
elif page == 'Project B':
    project.display_project_b()  # Memanggil Project B
elif page == 'Poem':
    poem.display_poem()

# **Setting Tampilan**
background.set_header_background()  
music.add_background_music("Across The Universe (Remastered 2009).mp3")  

# Tambahkan warna latar belakang transparan
st.markdown("""
    <style>
    .stApp {
        background-color: rgba(10, 10, 10, 0.8);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)