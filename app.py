from flask import Flask, render_template

app = Flask(__name__)

# Sample data
workout_groups = {
    "Short": [
        {
            "title": "2 x 2000m rate increase",
            "description": "2 x 2000m rate increase / 4 min easy  @2k + 8-10 (can go less at higher spm). <br> Row two 2000 meter pieces. In each piece, row the first 1000 meters @ 26 spm. Then 500 meters @ 28 spm, 250 meters @ 30 spm and 250 meters @ 32 spm. Row for four minutes at light pressure during the rest period.",
            "heart_rate_zone": "UT1",
            "total_time": "20 minutes"
        },
        {
            "title": "6 x 500m / 2:00 rest",
            "description": "6 x 500m / 2:00 rest @2k - 1 - 3 . <br> Row six 500 meter pieces. Row or rest for two minutes at light pressure between each 500.",
        }
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