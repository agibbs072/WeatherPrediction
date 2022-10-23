import pandas as pd
import pickle
import numpy as np
from django.contrib.staticfiles import finders


class Weather:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        csv_path = finders.find("seattle-weather.csv")
        # csv_path = "../static/seattle-weather.csv"
        self.weather_data = pd.read_csv(csv_path, index_col="date")
        self.weather_data = pd.DataFrame(self.weather_data)
        self.clean_data(self.weather_data)
        self.features = self.weather_data.drop(["precipitation", "temp_min", "temp_max", "wind", "weather"], axis=1)
        # the year, month, and day are the features the user will enter in the webapp
        self.features["year"] = self.features.index.str[:4].astype(int)
        self.features["month"] = self.features.index.str[5:7].astype(int)
        self.features["day"] = self.features.index.str[8:10].astype(int)
        self.conditions = {0: "drizzle", 1: "fog", 2: "rain", 3: "snow", 4: "sun"}

    def clean_data(self, data):
        data.dropna(inplace=True)
        # turn infinite values into NaN values and drop them
        data.replace([np.inf, -np.inf], np.nan).dropna(axis=0, inplace=True)

    def predict_condition(self, temp_min, temp_max, precipitation):
        """ predict the future weather condition based on year, month, day, temp min and max """
        with open(finders.find("weather_model.pkl"), "rb") as f:
            model = pickle.load(f)
            condition_value = model.predict(np.array([[
                self.year, self.month, self.day, temp_min, temp_max, precipitation
            ]]))

            condition = self.conditions[condition_value[0]]
            #print("Predicted Weather Condition: ", condition)

        return condition

    def predict_temperature(self, mode):
        """ predict the future temperature based on the year, month, and day """
        with open(finders.find("{}_model.pkl".format(mode)), "rb") as f:
            model = pickle.load(f)
            temp_value = int(model.predict(np.array([[self.year, self.month, self.day]]))[0])
            #print("Predicted {0}".format(mode), temp_value)

        return temp_value

    def get_precipitation_average(self):
        """ get the average precipitation for the month """
        graph = self.features
        graph["precipitation"] = self.weather_data["precipitation"]
        precipitation = 0
        if self.month == "january":
            precipitation = round(graph[graph["month"] == 1]["precipitation"].mean(), 1)
        elif self.month == "february":
            precipitation = round(graph[graph["month"] == 2]["precipitation"].mean(), 1)
        elif self.month == "march":
            precipitation = round(graph[graph["month"] == 3]["precipitation"].mean(), 1)
        elif self.month == "april":
            precipitation = round(graph[graph["month"] == 4]["precipitation"].mean(), 1)
        elif self.month == "may":
            precipitation = round(graph[graph["month"] == 5]["precipitation"].mean(), 1)
        elif self.month == "june":
            precipitation = round(graph[graph["month"] == 6]["precipitation"].mean(), 1)
        elif self.month == "july":
            precipitation = round(graph[graph["month"] == 7]["precipitation"].mean(), 1)
        elif self.month == "august":
            precipitation = round(graph[graph["month"] == 8]["precipitation"].mean(), 1)
        elif self.month == "september":
            precipitation = round(graph[graph["month"] == 9]["precipitation"].mean(), 1)
        elif self.month == "october":
            precipitation = round(graph[graph["month"] == 10]["precipitation"].mean(), 1)
        elif self.month == "november":
            precipitation = round(graph[graph["month"] == 11]["precipitation"].mean(), 1)
        elif self.month == "december":
            precipitation = round(graph[graph["month"] == 12]["precipitation"].mean(), 1)

        return precipitation



