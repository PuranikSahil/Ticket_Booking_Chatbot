import streamlit as st
import database


def show_admin():
    st.markdown(
        """
        <style>
        .stApp{
        background-image: url("https://marketplace.canva.com/EAF5FxQlSGQ/1/0/1600w/canva-blue-and-white-illustrated-sky-and-airplane-desktop-wallpaper-zYA4XGHAYo0.jpg");
        background-attachment: fixed;
        background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        pwd = st.text_input("password")
        if pwd == 'Abc123':
            with col3:
                with st.container(border=True):
                    st.markdown("<h2 style= 'text-align: center; font-style: italic';>Airline Index</h2>",unsafe_allow_html=True)
                    for i in range (len(database.airlines())):
                        st.text(f"{i+1} {database.airlines()[i]['airline_name']}")
            with col2:
                if st.button("Add flight"):
                    fno =st.text_input("flight_no")
                    ano =st.text_input("airline_no")
                    sd =st.text_input("source_dest")
                    td =st.text_input("target_dest")
                    dept = st.text_input("depart")
                    bus_pri =st.text_input("business_price")
                    eco_price =st.text_input("eco_price")
                    if fno and ano and sd and td and dept and bus_pri and eco_price:
                        database.add_flight(fno,ano,sd,td,dept,bus_pri,eco_price)


        else:
            st.error("Wrong Pass")