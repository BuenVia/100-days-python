import requests, datetime, os

APP_ID=os.environ.get("APP_ID")
API_KEY=os.environ.get("API_KEY")
AUTH_KEY=os.environ.get("AUTH_KEY")

sheety_endpoint = "https://api.sheety.co/1b44c2fc74da196fc5e0fa22856b14ca/workoutTracking/sheet1"

GENDER = "male"
HEIGHT = 186
WEIGHT = 104
AGE = 38

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": 0
}

exercise_input = input("How far did you run?: ")

parameters = {
 "query": exercise_input,
 "gender":GENDER,
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=parameters)
response.raise_for_status()
exercises = response.json()

for exercise in exercises['exercises']:
    today = datetime.datetime.now()
    date = today.strftime('%d/%m/%Y')
    time = today.strftime("%X")
    print(date)

    sheety_body = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    headers = {
        "Authorization": AUTH_KEY
    }

    sheety_response = requests.post(sheety_endpoint, json=sheety_body, headers=headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)