from django.urls import path
from django.contrib import admin
from .views import show_account
from .views import login_register
from .views import login
from .views import logout
from .views import register
from .views import change_password
from .views import save_profile


urlpatterns = [

	path('', 					show_account , name='show_account'),
	path('login-reg-form/', 	login_register , name='login_register'),
	path('login/', 				login , name='login'),
	path('logout/', 			logout , name='logout'),
	path('register/', 			register , name='register'),
	path('change-password/',	change_password , name='change_password'),
	path('save-profile/', 		save_profile , name='save_profile'),

]