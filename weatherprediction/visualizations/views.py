import plotly.express as px
from django.shortcuts import render
from dash import dcc, html
from django_plotly_dash import DjangoDash
from .WeatherStatistics import WeatherStatistics


app = DjangoDash("Visualizations")
stats = WeatherStatistics()

data = stats.get_temp_data()
temp_fig = px.line(
    data, title="Average Max Temperature By Month",
    x=data["month"], y=data["avg_temp"],
    labels={"avg_temp": "average temperature(celsius)"}
)

data = stats.get_weather_data()
weather_fig = px.histogram(
    data, title="Frequency of Weather Conditions across all years", x=data["weather"],
    color="weather"
)

data = stats.get_precipitation_data()
prcp_fig = px.line(
    data, title="Average Precipitation by Month", x=data["month"],
    y=data["avg_prcp"], markers=True, labels={"avg_prcp": "average precipitation(millimeters)"}
)

# each graph on the visualization page
app.layout = html.Div(
    children=[
        dcc.Graph(
            figure=temp_fig
        ),
        dcc.Graph(
            figure=weather_fig
        ),
        dcc.Graph(
            figure=prcp_fig
        )
    ]
)


def index(request):
    template = "visualizations/index.html"
    return render(request, template, {})
