from flask import Flask, render_template

app = Flask(__name__)

# Sample data
workout_groups = {
    "Short": [
        {
            "title": "5 x 500m, 2’ easy paddle",
            "description": "5 x 500m, 2’ easy paddle (no stop) @2k-3",
            "heart_rate_zone": "AT",
            "total_time": "~18’ + WU/CD"
        },

        {
            "title": "5000m with rate changes",
            "description": "5000m with rate changes every 1000m: 25-22-25-28-25",
            "heart_rate_zone": "UT1",
            "total_time": "~20’"
        },

        {
            "title": "5 x 3 min / 1 min easy",
            "description": "5 x 3 min / 1 min easy @ 2k + 4",
            "heart_rate_zone": "AT",
            "total_time": "~20’ + WU/CD"
        },

        {
            "title": "Stroke pyramid",
            "description": "Stroke pyramid: 10/20/30/40/50/40/30/20/10 Take 10 strokes hard followed by 10 light. Then take 20 strokes hard followed by 20 light. 30 hard, 30 light. 40-40. 50-50. 40-40. 30-30. 20-20. 10-10 (hard @2k, easy paddle)",
            "heart_rate_zone": "UT1",
            "total_time": "~20’ + WU/CD"
        },

        {
            "title": "2 x 2000m rate increase",
            "description": "2 x 2000m rate increase / 4 min easy @2k + 8-10 (can go less at higher spm). Row two 2000 meter pieces. In each piece, row the first 1000 meters @ 26 spm. Then 500 meters @ 28 spm, 250 meters @ 30 spm and 250 meters @ 32 spm. Row for four minutes at light pressure during the rest period.",
            "heart_rate_zone": "UT1",
            "total_time": "~22’ + WU/CD"
        },

        {
            "title": "21 minutes with rate increase",
            "description": "21 minutes with rate increase @ 2k + 18-20 (decreasing time by 2 sec every rate increase) Row the first six minutes @ 20 spm. Then row five minutes @ 22 spm, four @ 24, three @ 26, two @ 28 and one @ 30.",
            "heart_rate_zone": "UT1-AT",
            "total_time": "21’ + WU/CD"
        },

        {
            "title": "4 x 1000m / 1 min easy/rest",
            "description": "4 x 1000m / 1 min easy/rest @ 2k + 6-8",
            "heart_rate_zone": "UT1",
            "total_time": "20’ + WU/CD"
        },

        {
            "title": "6x500m / 2’ rest",
            "description": "6x500m / 2’ rest @ 2k - 1-3. Every time you do this remove 15” rest (like separate days)",
            "heart_rate_zone": "AT",
            "total_time": "20’ + WU/CD"
        },

        {
            "title": "10 x 1 min / 1 min easy",
            "description": "10 x 1 min / 1 min easy @ 2k - 3-4",
            "heart_rate_zone": "AN",
            "total_time": "20’ + WU/CD"
        },

        {
            "title": "13 x 30” flat out",
            "description": "13 x 30” flat out with 15” rest (so 6:30 total work) - up to 3 sets with 4’ rest between them",
            "heart_rate_zone": "AN",
            "total_time": "15’ - 25’ + WU/CD"
        },

        {
            "title": "30’ @ 2k + 10-14",
            "description": "30’ @ 2k + 10-14",
            "heart_rate_zone": "UT1",
            "total_time": "30’"
        },

        {
            "title": "5x (1’ @2k + 2, 1’ @2k - 2)",
            "description": "5x (1’ @2k + 2, 1’ @2k - 2). 90” rest in between each round.",
            "heart_rate_zone": "AT",
            "total_time": "17.5’ + WU/CD"
        },

        {
            "title": "10 bullet",
            "description": "10 bullet (10x 1’ @2k- 2-4 with 1’ rest)",
            "heart_rate_zone": "AN",
            "total_time": "20’ + WU/CD"
        },

        {
            "title": "1/2/3/4/5/6’ with 1’ rest",
            "description": "1/2/3/4/5/6’ with 1’ rest @2k + 4-8",
            "heart_rate_zone": "AT",
            "total_time": "26’"
        },

        {
            "title": "Ergocalypse",
            "description": "Ergocalypse [14 x 250m @ 2k - 3-4 with 1’ rest. Open Rate.]",
            "heart_rate_zone": "AN",
            "total_time": "30’ + WU/CD"
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