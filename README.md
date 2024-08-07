# Erg Workouts
Erg workouts 

## Website
https://ergworkouts.com

## Installation

For static site
`python generate_static.py`
For dynamic site
`python app.py`

This website is generated through a [GitHub Action cronjob](https://github.com/mediantre/erg4life/blob/main/.github/workflows/main.yml) which gets the new workout of the day from concept2 and the workouts 

## Contributing

Contributions are always welcome!

See [contributing.md](contributing.md) for ways to get started.
### How to report a bug

Create an issue [here](https://github.com/mediantre/erg4life/issues)

### How to add workouts

Workouts are stored in erg_workouts.json. 

The format is as following:

```json
{
    "title": "title of the workout",
    "description": "description of the workout",
    "heart_rate_zone": "heart rate zone (UT1, UT2, UT3, AT, TR, AN)",
    "total_time": "total time of the workout (string)",
}
```

You can add workouts by creating a pull request

There are plans to add a more categorical way of representing workouts using the [Concept2 ERG format](https://log.concept2.com/developers/validator). This will be added in the future.

There are also plans to add a way to add workouts using the website. This will be added in the future.

## Acknowledgements

[Concept2](https://log.concept2.com/)
