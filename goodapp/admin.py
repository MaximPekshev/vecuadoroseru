from django.contrib import admin

from 	.models 	import Good
from 	.models 	import Picture
from authapp.models import Buyer


class PictureInline(admin.TabularInline):
    model = Picture

    extra = 0


class GoodAdmin(admin.ModelAdmin):
	list_display = (
					'name', 
					'vendor_code',
					'slug',
					)
	
	inlines 	 = [PictureInline]

admin.site.register(Good, GoodAdmin)



class PictureAdmin(admin.ModelAdmin):
	list_display = (
					'title', 
					'good',
					)

	list_filter = (
					'good', 
					)

admin.site.register(Picture, PictureAdmin)

class BuyerAdmin(admin.ModelAdmin):
	list_display = (
					'user', 
					'first_name',
					'last_name',
					'Phone',
					'address',
					)

admin.site.register(Buyer, BuyerAdmin)

