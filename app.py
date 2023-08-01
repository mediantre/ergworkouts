from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)

# Load data into workout_groups from json file (erg_workouts.json)
with open('erg_workouts.json', 'r', encoding='utf-8') as f:
    workout_groups = json.load(f)

# pick a random workout from the list

workout_of_the_day = random.choice(workout_groups[random.choice(list(workout_groups.keys()))])

workout_of_the_day = "{} ○ \nDescription: {} ○ \nHeart Rate Zone: {} ○ \nTotal Time: {}".format(
    workout_of_the_day['title'],
    workout_of_the_day['description'],
    workout_of_the_day['heart_rate_zone'],
    workout_of_the_day['total_time']
)


# https://api-v4.concept2.com/wod/today
c2_workout_of_the_day = json.loads(requests.get('https://api-v4.concept2.com/wod/today').text)["description"]["en"]

@app.route('/')
def index():
    return render_template('erg_workouts.html', workout_groups=workout_groups, workout_of_the_day=workout_of_the_day, c2_workout_of_the_day=c2_workout_of_the_day)

if __name__ == '__main__':
    app.run(debug=True)