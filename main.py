import streamlit as st
from database import supabase

def show_main():
    st.markdown(
        """
        <style>
        .stApp{
        background-image: url("https://imageio.forbes.com/specials-images/imageserve/66ba827c8ff2be58a5e1ea62/Aircraft-landing-at-sunrise/0x0.jpg?format=jpg&width=480");
        background-attachment: fixed;
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    col1,col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style = 'text-align: center;color: #FF4B4B; font-style: italic';>GO BOOKINGS </h2>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;color: #FF4B4B;font-style: italic'> Book Your Flight Tickets!</h2>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col2:
        st.markdown("<h2 style='text-align: center;color: #FF4B4B;font-style: italic'> Today!</h2>", unsafe_allow_html=True)


    col1,col2,col3,col4 = st.columns(4)

    with col2:
        if st.button("Log in"):
            st.session_state.logged_in = 1
            st.rerun()

    with col3:
        if st.button("Register!"):
            st.session_state.logged_in = 2
            st.rerun()
    with col4:
        if st.button("Admin Login"):
            st.session_state.logged_in = 4
            st.rerun()