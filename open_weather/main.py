import requests
import os
from twilio.rest import Client

API_KEY = "1b4285cacb852ff76f4aa122cc7bc8d1"
account_sid = 'AC1c6aee0b64379f2a3d9a8436ec0e0f34'
auth_token = '697c98fca8a56b8e2ec3d127388d850b'

weather_params = {
    "lat": -39.642799,
    "lon": 176.843994,
    "appid": API_KEY,
}

will_rain = False

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()["list"][0:12]
for period in weather_data:
    condition_code = period["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Bring your umbrella.",
                     from_='+18788796449',
                     to='+447708913089'
                 )

print(message.status)