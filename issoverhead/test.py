import requests
from datetime import datetime

MY_LAT = 51.903763
MY_LONG = 0.196612

parameters ={
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')
sunset = data['results']['sunset']

print(sunrise)

# time_now = datetime.now()

# print(time_now)