from django.urls import path, include

urlpatterns = [
    path("", include("forecast.urls")),
    path("visualizations/", include("visualizations.urls")),
    path('plotly_graphs/', include('django_plotly_dash.urls')),
]
