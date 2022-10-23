import calendar
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import render
from .WeatherPredictions import Weather


template = "forecast/index.html"


def index(request):
    # get the current date and transform it into year, month, day; save the day of the week to a variable
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    # get the initial day of the week as a value and define the loop count and week list
    count = 6
    name_value = datetime.now().weekday()
    week = []

    while count >= 0:
        # send the year, month, day to the backend
        weather = Weather(year, month, day)
        temp_max = weather.predict_temperature("temp_max")
        temp_min = weather.predict_temperature("temp_min")
        condition = weather.predict_condition(
            temp_max, temp_min, weather.get_precipitation_average()
        )
        name = calendar.day_name[name_value].lower()
        name_value = (name_value + 1) % 7
        count -= 1
        day = (datetime.now() + timedelta(days=1)).day
        month = (datetime.now() + timedelta(days=1)).month
        year = (datetime.now() + timedelta(days=1)).year
        week.append({
            "name": name, "temp_max": temp_max, "temp_min": temp_min,
            "condition": "forecast/images/{}.png".format(condition)
        })

    return render(request, template, {"week": week})


def custom_forecast(request):
    year = int(request.POST["year"])
    month = int(request.POST["month"])
    day = int(request.POST["day"])
    weather = Weather(year, month, day)
    temp_max = weather.predict_temperature("temp_max")
    temp_min = weather.predict_temperature("temp_min")
    condition = weather.predict_condition(
        temp_max, temp_min, weather.get_precipitation_average()
    )
    name_value = datetime(year, month, day).weekday()
    name = calendar.day_name[name_value].lower()
    cf = {
        "name": name, "temp_max": temp_max, "temp_min": temp_min,
        "condition": "forecast/images/{}.png".format(condition)
    }

    return JsonResponse({"custom_forecast": cf})

