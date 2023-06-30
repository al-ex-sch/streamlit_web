import streamlit as st
import about
import project_a
import project_b
import contact
import projects

# Sidebar menu with radio buttons
menu = st.sidebar.radio("Menu", ["About Me", "Projects", "Contact"])

# Initialize session_state for navigation
if "project_page" not in st.session_state:
    st.session_state.project_page = None

# Content based on menu selection
if menu == "About Me":
    about.display()

elif menu == "Projects":
    # Check session state for project details navigation
    if st.session_state.project_page == "project_a":
        project_a.display()
    elif st.session_state.project_page == "project_b":
        project_b.display()
    else:
        projects.display()

elif menu == "Contact":
    contact.display()
