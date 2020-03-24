from django.urls import path
from django.contrib import admin
from .views import show_cart
from .views import cart_add_item
from .views import cart_del_item
from .views import cart_checkout
from .views import place_order

urlpatterns = [

	path('', 					show_cart , name='show_cart'),
	path('add/<str:slug>/',		cart_add_item, 	name = 'cart_add_item'),
	path('del/<str:slug>/',		cart_del_item, 	name = 'cart_del_item'),
	path('checkout/',			cart_checkout, 	name = 'cart_checkout'),
	path('place-order/',		place_order, 	name = 'place_order'),

]