import pandas as pd
import numpy as np
from django.contrib.staticfiles import finders


class WeatherStatistics:
    def __init__(self):
        csv_path = finders.find("seattle-weather.csv")
        #csv_path = "../static/seattle-weather.csv"
        self.weather_data = pd.read_csv(csv_path, index_col="date")
        self.weather_data = pd.DataFrame(self.weather_data)
        self.clean_data(self.weather_data)
        self.features = self.weather_data.drop(["precipitation", "temp_min", "temp_max", "wind", "weather"], axis=1)
        # the year, month, and day are the features the user will enter in the webapp
        self.features["year"] = self.features.index.str[:4].astype(int)
        self.features["month"] = self.features.index.str[5:7].astype(int)
        self.features["day"] = self.features.index.str[8:10].astype(int)

    def clean_data(self, data):
        data.dropna(inplace=True)
        # turn infinite values into NaN values and drop them
        data.replace([np.inf, -np.inf], np.nan).dropna(axis=0, inplace=True)

    def get_temp_data(self):
        """ get the average temperature for each month """
        graph = self.features
        graph["temp_max"] = self.weather_data["temp_max"]
        jan_temp = round(graph[graph["month"] == 1]["temp_max"].mean(), 1)
        feb_temp = round(graph[graph["month"] == 2]["temp_max"].mean(), 1)
        mar_temp = round(graph[graph["month"] == 3]["temp_max"].mean(), 1)
        apr_temp = round(graph[graph["month"] == 4]["temp_max"].mean(), 1)
        may_temp = round(graph[graph["month"] == 5]["temp_max"].mean(), 1)
        jun_temp = round(graph[graph["month"] == 6]["temp_max"].mean(), 1)
        jul_temp = round(graph[graph["month"] == 7]["temp_max"].mean(), 1)
        aug_temp = round(graph[graph["month"] == 8]["temp_max"].mean(), 1)
        sep_temp = round(graph[graph["month"] == 9]["temp_max"].mean(), 1)
        oct_temp = round(graph[graph["month"] == 10]["temp_max"].mean(), 1)
        nov_temp = round(graph[graph["month"] == 11]["temp_max"].mean(), 1)
        dec_temp = round(graph[graph["month"] == 12]["temp_max"].mean(), 1)
        data = {
            "month": [
                "january", "february", "march", "april",
                "may", "june", "july", "august", "september",
                "october", "november", "december"
            ],
            "avg_temp": [
                jan_temp, feb_temp, mar_temp, apr_temp, may_temp,
                jun_temp, jul_temp, aug_temp, sep_temp, oct_temp,
                nov_temp, dec_temp
            ]
        }
        temps = pd.DataFrame(data)
        return temps

    def get_weather_data(self):
        """ Frequency of weather conditions in the Seattle area """
        graph = self.weather_data.drop(["precipitation", "temp_min", "temp_max", "wind"], axis=1)
        return graph

    def get_precipitation_data(self):
        graph = self.features
        graph["precipitation"] = self.weather_data["precipitation"]
        jan_prcp = round(graph[graph["month"] == 1]["precipitation"].mean(), 1)
        feb_prcp = round(graph[graph["month"] == 2]["precipitation"].mean(), 1)
        mar_prcp = round(graph[graph["month"] == 3]["precipitation"].mean(), 1)
        apr_prcp = round(graph[graph["month"] == 4]["precipitation"].mean(), 1)
        may_prcp = round(graph[graph["month"] == 5]["precipitation"].mean(), 1)
        jun_prcp = round(graph[graph["month"] == 6]["precipitation"].mean(), 1)
        jul_prcp = round(graph[graph["month"] == 7]["precipitation"].mean(), 1)
        aug_prcp = round(graph[graph["month"] == 8]["precipitation"].mean(), 1)
        sep_prcp = round(graph[graph["month"] == 9]["precipitation"].mean(), 1)
        oct_prcp = round(graph[graph["month"] == 10]["precipitation"].mean(), 1)
        nov_prcp = round(graph[graph["month"] == 11]["precipitation"].mean(), 1)
        dec_prcp = round(graph[graph["month"] == 12]["precipitation"].mean(), 1)
        data = {
            "month": [
                "january", "february", "march", "april",
                "may", "june", "july", "august", "september",
                "october", "november", "december"
            ],
            "avg_prcp": [
                jan_prcp, feb_prcp, mar_prcp, apr_prcp, may_prcp,
                jun_prcp, jul_prcp, aug_prcp, sep_prcp, oct_prcp,
                nov_prcp, dec_prcp
            ]
        }
        prcp = pd.DataFrame(data)
        return prcp



