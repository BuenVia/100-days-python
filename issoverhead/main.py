import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.903763 # Your latitude
MY_LONG = -0.196612 # Your longitude
MY_EMAIL = "biffbuchanan1985@gmail.com"
MY_PASSWORD = "ttqlmucjwavxzxza"

def iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss = response.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if iss_latitude < MY_LAT + 5 and iss_latitude > MY_LAT - 5 and iss_longitude < MY_LONG + 5 and iss_longitude > MY_LONG - 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_sun = response.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True

while True:
    time.sleep(60)
    if iss_nearby() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="matthewclifford@hotmail.co.uk",
            msg=f"Subject: Look up!\n\nLook up!!! The ISS is at LAT: {MY_LAT} LONG: {MY_LONG}"
        )
