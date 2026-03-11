import streamlit as st
import  flight_bot
import flight_Intent_Response
import random
import database
import login
import re




def show_entry():
    flg = 0
    user_name = st.session_state.username
    uid = database.id(user_name)

    st.set_page_config("Welcome!")
    def show_tick_dets (ticket_number,flight_num,airline,source,target,date,timer,seat_class,price_paid):
        colx,coly = st.columns(2)
        with coly:
            with st.container(border=True):
                st.markdown("<h2 style = 'text-align: center;color: #FF4B4B; font-style: italic';>TICKET DETAILS </h2>",unsafe_allow_html=True)
                st.text(f"Ticket Number: {ticket_number} ")
                st.text(f"Flight number:{flight_num} ")
                st.text(f"Airline: {airline} ")
                st.text(f"Source: {source} ")
                st.text(f"Target: {target} ")
                st.text(f"Date: {date} ")
                st.text(f"Time: {timer} ")
                st.text(f"Seat Class: {seat_class} ")
                st.text(f"Price: {price_paid} ")

    try:
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
        st.markdown("<h3 style = 'text-align: center;; font-style: italic';>Hello There! I will be guiding you to book your tickets! </h3>",
                        unsafe_allow_html=True)
        coli1,coli2 = st.columns(2)
        flag = 0
        with coli1:
            with st.container(border=True):
                st.text("How can i help you?")
                user_input = st.text_input(f"User ({uid}): ")
                if user_input:
                    intent, confidence = flight_bot.predict_intent(user_input)
                    # Intent action
                    st.text(flight_Intent_Response.BOT_RESPONSES[intent][random.randint(0, len(intent))])
                    flag = 1
                if flag == 1:
                    #--------------------------------#
                    if intent == 'BOOK_FLIGHT':
                        source = st.text_input("From: ")
                        target = st.text_input("To: ")
                        date = st.date_input("Date: ")
                        if source and target:
                            col1,col2 = st.columns(2)
                            with col1:
                                st.text("Flight number: ")
                                st.text("Airline: ")
                                st.text("Buisness Class: ")
                                st.text("Economy Class: ")
                            with col2:
                                flight_num = database.get_flights(source, target)
                                if flight_num:
                                    fno = flight_num[0]['flight_no']
                                    st.text(fno)
                                    ano = database.get_airline_num(fno)[0]['airline_num']
                                    airline = database.get_airline(ano)
                                    st.text(airline[0]['airline_name'])
                                    business = st.button(f"{database.get_ticket_prices(fno)[0]['business_price']}₹")
                                    economy = st.button(f"{database.get_ticket_prices(fno)[0]['economy_price']}₹")
                                    if business:
                                        st.success("HOORAY TICKET BOUGHT!")
                                        ticket_num = database.ticket_num()[0]['ticket_no'] + 1
                                        database.buy_ticket(ticket_num,uid,fno,seat_class='BUSINESS',price_paid=database.get_ticket_prices(fno)[0]['business_price'])
                                        flg = 1

                                    if economy:
                                        st.success("HOORAY TICKET BOUGHT!")
                                        ticket_num = database.ticket_num()[0]['ticket_no'] + 1

                                        database.buy_ticket(ticket_num,uid, fno, seat_class='ECONOMY',
                                                            price_paid=database.get_ticket_prices(fno)[0][
                                                                'economy_price'])
                                        flg = 2

                                else:
                                    st.text("No flights found")
                                    st.text("None")
                    # --------------------------------------------------------------------#
                    elif intent == "CANCEL_BOOKING":
                        tno = st.text_input("Enter your ticket number")
                        if tno:
                            if database.search_ticket(tno):
                                tpid = database.search_ticket(tno)['passenger_id']
                                if tpid == uid:
                                    database.cancel_booking(tno)
                                    st.text("CANCELED BOOKING!")
                                else:
                                        st.error("Dont ruin other's experience!")
                            else:
                                st.error("No such ticket number exists")
                    # --------------------------------------------------------------------#
                    elif intent == "FLIGHT_DETAILS" or "TICKET_DETAILS":
                        fno = st.text_input("Enter Flight Number:")
                        tno = st.text_input ("Enter Ticket Number:")
                        if fno and tno:
                            if (uid == database.search_ticket(tno)['passenger_id']) and (int(fno) == database.search_ticket(tno)['flight_no']):
                                flg = 3
                            else:
                                st.error("Details mismatch!")







    except:
        st.error("Sorry, i didn't understand... could you be more specific?")

    with coli2:
        if flg == 1:
            timer = database.get_flights(source,target)[0]['departure']
            timer = timer.split('T')[1]
            show_tick_dets(ticket_num,fno, airline[0]['airline_name'], source, target, date, timer, seat_class='Business',
                           price_paid=database.get_ticket_prices(fno)[0]['business_price'])
        if flg == 2:
            show_tick_dets(ticket_num,uid,fno, airline[0]['airline_name'], source, target, date, seat_class='Economy',
                           price_paid=database.get_ticket_prices(fno)[0]['economy_price'])

        if flg == 3:
            if database.flight_det(fno):
                with st.container(border = True):
                    date_ = database.flight_det(fno)[0]['departure']
                    time = date_.split('T')[1]
                    date_ = date_.split('T')[0]
                    ano = database.flight_det(fno)[0]['airline_num']
                    st.text(f"From: {database.flight_det(fno)[0]['source_dest']}")
                    st.text(f"To: {database.flight_det(fno)[0]['target_dest']}")
                    st.text(f"Date: {date_}")
                    st.text(f"Time: {time}")
                    st.text(f"Airline: {database.get_airline(ano)[0]['airline_name']}")
                    st.text(f"Price paid: {database.search_ticket(tno)['price_paid']}")
                    st.text(f"Seat type: {database.search_ticket(tno)['seat_class']}")
