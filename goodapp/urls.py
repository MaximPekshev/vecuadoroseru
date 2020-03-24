from django.urls import path
from django.contrib import admin
from .views import show_catalog


urlpatterns = [

	path('', 				show_catalog , name='show_catalog'),
	
]