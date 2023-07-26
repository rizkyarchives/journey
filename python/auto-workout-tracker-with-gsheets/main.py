import requests
import os
from datetime import datetime

# HOW TO SET ENV VARIABLES IN VSCODE?
# HERE IS THE COMMAND TO WRITE IN THE TERMINAL : setx KEY "VALUE"
# DO RESTART YOUR VSCODE FOR THE ENVIRONMENT VARIABLES THAT YOU'VE SET UP TO APPEAR. THAT'S IT!

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
EXERCISE_LINK = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEET_LINK = 'https://api.sheety.co/1ebf3597aebdfd2429f2c8a2b623cb91/myWorkoutsTracker/workouts'
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

prompt = input("What exercises did you do? ")

authentication = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

request_config = {
    "query": prompt,
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 164,
    "age": 19
}

response = requests.post(url=EXERCISE_LINK, headers=authentication, json=request_config)
datas = response.json()
current_time = datetime.now()
formatted_time = current_time.strftime('%d/%m/%Y')
clock = current_time.strftime('%H:%M:%S')
header = {
    "Authorization": "Bearer DAMNNOACCESS?HAHA",
    "Content-Type": "application/json"
}
for data in datas["exercises"]:
    row_content = {
        "workout": {
            "date": formatted_time,
            "time": clock,
            "exercise": data["name"].capitalize(),
            "duration": str(data["duration_min"]),
            "calories": str(data["nf_calories"])
        }
    }
    response = requests.post(url=SHEET_LINK, json=row_content, headers=header)
    print(response.text)

