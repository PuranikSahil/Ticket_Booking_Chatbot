import streamlit as st
from main import show_main
from register_page import show_register_page
from login import show_login
from entry import show_entry
from admin import show_admin


st.set_page_config("GO BOOKINGS")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = 0

#login_pg = st.Page("Login.py", title="Login")
main = st.Page("main.py")
login_page = st.Page("login.py")
register = st.Page("register_page.py")
entry_page = st.Page("entry.py")


if st.session_state.logged_in == 0:
    show_main()
elif st.session_state.logged_in == 1:
    show_login()
elif st.session_state.logged_in == 2:
    show_register_page()
elif st.session_state.logged_in == 3:
    show_entry()
elif st.session_state.logged_in == 4:
    show_admin()


