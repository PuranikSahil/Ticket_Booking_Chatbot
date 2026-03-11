import streamlit as st
from database import find_user,put_user,max_id


def show_register_page():
    st.title("Register..")
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

    new_id = max_id()+1

    name = st.text_input("Enter your name")

    age = st.text_input("Enter your age")
    if age:
        try:
            age = int(age)
        except ValueError:
            st.error("Age must be an integer")
    new_user = st.text_input("Enter your username: ")

    if new_user:
        if find_user(new_user):
            st.error("Username already exists, try another one")
        else:
            st.success("Username {new_user} is available".format(new_user=new_user))


    new_pwd = st.text_input("Enter your password: ",type="password")
    if new_pwd:
        if len(new_pwd) < 4:
            st.error("Password must be at least 4 characters")
    if new_id and name and age and new_pwd and new_user:
        if st.button("Register"):
            put_user(new_id, name, age, new_user, new_pwd)
            st.write("You have successfully registered")
            current_user = name
            st.session_state.logged_in = 1
            st.rerun()
