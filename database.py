import os
from supabase import create_client,Client
from dotenv import load_dotenv

load_dotenv()
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def find_user(username):
    response =(supabase
               .table('passengers')
               .select('*')
               .eq("username", username)
               .execute()
    )
    if response.data:
        return response.data[0]
    else:
        return None

def id(username):
    response = (supabase
                .table('passengers')
                .select('*')
                .eq("username", username)
                .execute())
    return response.data[0]['id']

def name(username):
    response = (supabase
                .table('passengers')
                .select('*')
                .eq('username',username)
                .execute()
    )
    if response.data:
        return response.data[0]['name']
    else:
        return None


def find_pwd(username):
    response = (supabase
                .table('passengers')
                .select('*')
                .eq("username", username)
                .execute()
    )
    if response.data:
        return response.data[0]

def max_id():
    response = (supabase
                .table('passengers')
                .select('id')
                .order('id',desc = True)
                .limit(1)
                .execute()
    )
    return response.data[0]['id']



def put_user(id,name,age,username,password):
    response = (supabase
                .table('passengers')
                .insert({
                    "id":id,
                    "name": name,
                    "age":age,
                    "username":username,
                    "password":password
                })
                .execute())
    return None

def get_flights(source,target):
    response =(supabase
               .table('flights')
               .select('*')
               .eq("source_dest", source)
               .eq("target_dest", target)
               .execute()
    )
    return response.data

#gives airline_num for the given flight number
def get_airline_num(num):
    response = (supabase
                .table('flights')
                .select('airline_num')
                .eq("flight_no", num)
                .limit(1)
                .execute()
                )
    return response.data


# gives airline for given number
def get_airline(num):
    response = (supabase
                .table('airlines')
                .select('*')
                .eq("airline_num", num)
                .execute()
                )
    return response.data

def get_ticket_prices(flight_number):
    response = (supabase
                .table('flights')
                .select('*')
                .eq('flight_no', flight_number)
                .execute()
    )
    return response.data

def ticket_num():
    response = (supabase
                .table('tickets')
                .select("*")
                .order("ticket_no", desc = True)
                .limit(1)
                .execute()
                )
    return response.data



def buy_ticket(ticket_no,passenger_id,flight_no,seat_class,price_paid):
    response = (supabase
                .table('tickets')
                .insert({
                "ticket_no":ticket_no,
                "passenger_id":passenger_id,
                "flight_no":flight_no,
                "seat_class":seat_class,
                "price_paid":price_paid
                })
                .execute()
                )
    return ("Successfully booked the ticket!")

def cancel_booking(ticket_no):
    response = (supabase
                .table('tickets')
                .delete()
                .eq("ticket_no", ticket_no)
                .execute()
                )
    return response.data

def search_ticket(ticket_no):
    response = (supabase
                .table('tickets')
                .select("*")
                .eq("ticket_no", ticket_no)
                .execute()
                )
    if response.data:
        return response.data[0]

def flight_det(fno):
    response = (supabase
                .table('flights')
                .select("*")
                .eq("flight_no", fno)
                .execute()
                )
    return response.data


#-----------------------------------#
def add_flight(fno,airline_no,source_dest,target_dest,depart,business_price,eco_price):
    response = (supabase
                .table('flights')
                .insert({
        "flight_no":fno,
        "airline_no":airline_no,
        "source_dest":source_dest,
        "target_dest":target_dest,
        "depart":depart,
        "seat_capacity": 180,
        "business_capacity":80,
        "business_available":80,
        "economy_capacity":100,
        "economy_available":100,
        "business_price":business_price,
        "eco_price":eco_price
    })
                .execute()
                )
    return  ("Added flight successfully!")


def airlines():
    response = (supabase
                .table('airlines')
                .select("*")
                .execute()
                )
    return response.data