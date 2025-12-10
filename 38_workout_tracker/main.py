import requests, os, datetime

CALORIE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

USER_WEIGHT = 75
USER_HEIGHT = 182
USER_AGE = 35
USER_GENDER = "male"

calorie_header = {
    "x-app-id": os.environ["NUTRITION_ID"],
    "x-app-key": os.environ["NUTRITION_KEY"],
}

sheety_header = {
    "Authorization": "Bearer " + os.environ["SHEETY_TOKEN"],
}

def exercise_to_calories():
    exercise = input("Tell me which exercises you did: ")
    calorie_parameters = {
        "query": exercise,
        "weight_kg": USER_WEIGHT,
        "height_cm": USER_HEIGHT,
        "age": USER_AGE,
        "gender": USER_GENDER,
    }
    submitted_exercise = requests.post(CALORIE_ENDPOINT, json=calorie_parameters, headers=calorie_header)
    submitted_exercise.raise_for_status()
    calorie_data = submitted_exercise.json()
    return calorie_data

def write_to_sheet():
    data = exercise_to_calories()
    for entries in data["exercises"]:
        sheety_parameters = {
            "workout": {
                "date": datetime.date.today().strftime("%d/%m/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M"),
                "exercise": entries["name"].title(),
                "duration": int(entries["duration_min"]),
                "calories": int(entries["nf_calories"]),
            }
        }
        append_line = requests.post(SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_header)
        append_line.raise_for_status()

write_to_sheet()