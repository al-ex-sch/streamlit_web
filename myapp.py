import streamlit as st
import about
import contact
import projects

menu = st.sidebar.radio("Menu", ["About Me", "Projects", "Contact"])

if "project_page" not in st.session_state:
    st.session_state.project_page = None

if menu == "About Me":
    about.display()

elif menu == "Projects":
    if st.session_state.project_page == "project_a":
        project_a.display()
    elif st.session_state.project_page == "project_b":
        project_b.display()
    else:
        projects.display()

elif menu == "Contact":
    contact.display()
