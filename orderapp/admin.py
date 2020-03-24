from django.contrib import admin
from .models import Order, Order_Item
from cartapp.models import Cart, Cart_Item


class Order_ItemInline(admin.TabularInline):
    model = Order_Item

    extra = 0

class OrderAdmin(admin.ModelAdmin):
	list_display = (
					'buyer', 
					'summ',
					)
	
	inlines 	 = [Order_ItemInline]

admin.site.register(Order, OrderAdmin)


class Cart_ItemInline(admin.TabularInline):
    model = Cart_Item

    extra = 0

class CartAdmin(admin.ModelAdmin):
	list_display = (
					'user', 
					'summ',
					)
	
	inlines 	 = [Cart_ItemInline]

admin.site.register(Cart, CartAdmin)