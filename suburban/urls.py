from django.urls import path, include
from django.contrib import admin
from api.views import CityDetails

urlpatterns = [
	path('distance/',view = CityDetails.Distance),
	path('search/',view = CityDetails.StationDetails),
    path('getall/',view = CityDetails.ViewData),
    
]