from jinja2 import Environment, FileSystemLoader
import os
import app

# Define the Jinja2 Environment
env = Environment(loader=FileSystemLoader("templates"))

# Load the template
template = env.get_template("erg_workouts.html")

# Sample workout data (same as in the previous example)
workout_groups = app.workout_groups

# Render the template with the workout data
static_html = template.render(workout_groups=workout_groups, workout_of_the_day=app.workout_of_the_day)

# Write the rendered template to a static HTML file
with open("index.html", "w") as f:
    f.write(static_html)