from django.urls import path
from . import views

app_name = "forecast"

urlpatterns = [
    path("", views.index, name="forecast"),
    path("custom_forecast", views.custom_forecast, name="custom_forecast")
]
