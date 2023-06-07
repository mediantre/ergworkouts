from flask import Flask, render_template

app = Flask(__name__)

# Sample data
workout_groups = {
    "Short": [
        {
            "title": "2 x 2000m rate increase",
            "description": "Row two 2000 meter pieces...",
            "heart_rate_zone": "75-85%",
            "total_time": "20 minutes"
        },
        # Other short workouts...
    ],
    "Medium": [
        {
            "title": "Medium Workout 1",
            "description": "Description for medium workout...",
            "heart_rate_zone": "70-80%",
            "total_time": "40 minutes"
        },
        # Other medium workouts...
    ],
    "Long": [
        {
            "title": "Long Workout 1",
            "description": "Description for long workout...",
            "heart_rate_zone": "65-75%",
            "total_time": "60 minutes"
        },
        # Other long workouts...
    ],
}

workout_of_the_day = "6 x 500m / 2:00 rest"

@app.route('/')
def index():
    return render_template('erg_workouts.html', workout_groups=workout_groups, workout_of_the_day=workout_of_the_day)

if __name__ == '__main__':
    app.run(debug=True)