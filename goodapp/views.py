from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Good
from . models import Picture
from django.core.paginator import Paginator

from cartapp.views import get_cart_header


def calc_discount(good):
	
	discount = 100 - (good.price*100//good.old_price)
	return discount

class Item(object):
	
	good 		= Good
	images 		= Picture
	main_images = Picture


def show_catalog(request):

	goods_count=50

	if request.GET.get('id'):

		good = Good.objects.get(slug=request.GET.get('id'))

		pictures = Picture.objects.filter(good=good).order_by('-main_image')
		main_pictures = pictures[0]
		
		if good.old_price:
			discount = calc_discount(good) 
		else:
			discount = None	

		template_name = 'goodapp/product-details.html'

		context = {
			'good': good, 'pictures': pictures, 'main_pictures': main_pictures, 'discount': discount,
		}

		context.update(get_cart_header(request))

		return render(request, template_name, context)
