"""
This file can be executed by itself
this is useful for testing each model's accuracy


"""
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder


class TrainWeatherModels:
    def __init__(self):
        # the precipitation value is in millimeters (mm)
        # the temperature values are by default celsius
        # the average wind speed is in meters per second (m/s)
        csv_path = "../static/seattle-weather.csv"
        self.weather_data = pd.read_csv(csv_path, index_col="date")
        self.weather_data = pd.DataFrame(self.weather_data)
        self.clean_data(self.weather_data)
        print(self.weather_data.head())
        self.features = self.weather_data.drop(["precipitation", "temp_min", "temp_max", "wind", "weather"], axis=1)
        # the year, month, and day are the features the user will enter in the webapp
        self.features["year"] = self.features.index.str[:4].astype(int)
        self.features["month"] = self.features.index.str[5:7].astype(int)
        self.features["day"] = self.features.index.str[8:10].astype(int)

    def clean_data(self, data):
        data.dropna(inplace=True)
        # turn infinite values into NaN values and drop them
        data.replace([np.inf, -np.inf], np.nan).dropna(axis=0, inplace=True)

    def weather_model(self):
        """ train the model used to predict weather conditions with classification """
        # add the temp min and max features
        features = self.features
        features["temp_min"] = self.weather_data["temp_min"]
        features["temp_max"] = self.weather_data["temp_max"]
        features["precipitation"] = self.weather_data["precipitation"]
        # change the weather conditions(ex: drizzle, rain, etc.) into numerical values
        target = self.weather_data["weather"]
        encoder = LabelEncoder()
        target = encoder.fit_transform(target)

        features_train, features_test, target_train, target_test = train_test_split(features, target,
                                                                                    test_size=0.2)
        model = RandomForestClassifier(
            criterion="entropy", max_features=3, min_samples_leaf=3, min_samples_split=6, n_estimators=120
        )
        model.fit(features_train, target_train)
        print("Weather Model Accuracy: ", cross_val_score(model, features_test, target_test).mean() * 100)
        # commented the following out so it doesn't waste time creating a new file:
        #with open('../static/weather_model.pkl', 'wb') as f:
        #    pickle.dump(model, f)

    def temperature_model(self, mode):
        """ train the model used to predict temperature values with regression """
        # target is what we want to predict and mode could be temp_min or temp_max
        target = self.weather_data[mode]
        # create training and test datasets
        features_train, features_test, target_train, target_test = train_test_split(self.features, target,
                                                                                    test_size=0.2)
        # create a random forest regressor and train the model
        model = RandomForestRegressor()
        model.fit(features_train, target_train)
        # accuracy of the model
        print("{0} Model Accuracy: ".format(mode), cross_val_score(model, features_test, target_test).mean() * 100)
        # commented the following out so it doesn't waste time creating a new file:
        #with open('../static/{0}_model.pkl'.format(mode), 'wb') as f:
        #    pickle.dump(model, f)


train = TrainWeatherModels()
train.temperature_model("temp_max")
train.temperature_model("temp_min")
train.weather_model()

