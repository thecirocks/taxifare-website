import streamlit as st
import datetime
import numpy as np
import pandas as pd
import requests



'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

# #DATE
# date = st.date_input("Insert Date", datetime.date(2024, 8, 10))
# st.write("Date: ", date)

# #################################################################

# #TIME
# time = st.time_input("Insert time", datetime.time(8, 45, 00))
# st.write("Time: ", time)

# #################################################################

# date_time = date & time


# pickup_long = st.number_input("Insert pickup longitude:")
# pickup_lat = st.number_input("Insert pickup latitude:")
# drop_long = st.number_input("Insert dropoff longitude:")
# drop_lat = st.number_input("Insert dropoff latitude:")

with st.form(key="params_for_api"):
    date = st.date_input("Insert Date", datetime.date(2024, 8, 10))
    time = st.time_input("Insert time", datetime.time(8, 45, 00))
    date_time = f'{date} {time}'
    pickup_longitude = st.number_input('pickup longitude', value=40.7614327)
    pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
    dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
    dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
    pass_count = st.number_input("Insert quantity of passangers: ", value=1, min_value=1, max_value=4)
    button = st.form_submit_button(label="OK")




#################################################################

# pass_count = st.number_input("Insert quantity of passangers: ", value=1, min_value=1, max_value=4)
# st.write("Passangers: ", pass_count)


#################################################################

#button = st.form_submit_button(label="OK")

dic = {
    "pickup_datetime": date_time,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": pass_count
    }

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''



url = 'https://taxifare.lewagon.ai/predict'
#url = 'https://taxifare.lewagon.ai/'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

st.write(dic)

response = requests.get(url=url, params=dic)
dados = response.json()

# if response.status_code == 200:
#     dados = response.json()
#     print(dados)
# else:
#     print(f"Erro: {response.status_code}")
st.write(response.status_code)
st.write(dados)
pred = dados['fare']
print(pred)

st.header(f'Fare Amount: $ {round(pred, 2)}')
