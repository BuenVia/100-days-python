import requests

APP_ID='053a27e5'
API_KEY='857492f554ede2fbeea6d65e36c1309a'

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

# exercise_input = input("How far did you run?: ")

# parameters = {
#  "query": exercise_input,
#  "gender":GENDER,
#  "weight_kg":WEIGHT,
#  "height_cm":HEIGHT,
#  "age":AGE
# }

# response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=parameters)
# response.raise_for_status()
# exercise = response.json()

sheety_body = {
    "sheet": {
        "date": 1,
        "time": 2,
        "exercise": 3,
        "duration": 22,
        "calories": 10,
    }
}

sheety_response = requests.post(sheety_endpoint, json=sheety_body)
sheety_response.raise_for_status()
print(sheety_response.text)