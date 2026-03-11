import streamlit as st
import database


def show_login():

    st.markdown(
        """
        <style>
        .stApp{
        background-image:url("https://marketplace.canva.com/EAF5FxQlSGQ/1/0/1600w/canva-blue-and-white-illustrated-sky-and-airplane-desktop-wallpaper-zYA4XGHAYo0.jpg");
        background-attachment:fixed;
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    flag = 0
    st.title("Login ")
    username = st.text_input("Enter your username")
    if username:
        check = database.find_user(username)
        if check:
            if username == database.find_user(username)['username']:
                st.write("Username verified!")
                st.session_state.username = username
                flag = 0.5
        else:
            st.error("Username Incorrect!")

    pwd = st.text_input("Enter your password")
    if pwd:
        if pwd == database.find_pwd(username)['password']:
            if pwd == database.find_user(username)['password']:
                st.write("Password verified!")
                flag = 1
            else:
                st.error("Wrong password")

    if pwd and username:
        if flag == 1:
            if st.button("Login"):
                current_user = database.name(username)
                st.session_state.logged_in = 3
                st.rerun()
