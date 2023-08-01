# Contributing

## How to contribute

1. Fork this repository
2. Create a new branch for your contribution
3. Commit your changes
4. Push your changes to your fork
5. Submit a pull request

## How to report a bug

Create an issue [here](https://github.com/mediantre/erg4life/issues)

## How to add workouts

Workouts are stores in erg_workouts.json. 

The format is as following:

```json
{
    "title": "title of the workout",
    "description": "description of the workout",
    "heart_rate_zone": "heart rate zone (UT1, UT2, UT3, AT, TR, AN)",
    "total_time": "total time of the workout (string)",
}
```

You can add workouts by creating a pull request using the steps above. (How to contribute)

There are plans to add a more categorical way of representing workouts using the [Concept2 ERG format](https://log.concept2.com/developers/validator). This will be added in the future.

There are also plans to add a way to add workouts using the website. This will be added in the future.

