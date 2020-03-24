from django.shortcuts import render, redirect

import smtplib, os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio 
from email.mime.image import MIMEImage 

from django.http import HttpResponse
from cartapp.views import get_cart_header
from goodapp.views import Item, calc_discount
from cartapp.models import Cart_Item
from goodapp.models import Good, Picture
from authapp.models import Buyer
from .forms import GetPriceForm



def show_index(request):
	
	goods = Good.objects.all().filter(is_catalog=False)

	table = []

	for good in goods:

		item = Item()
		
		item.good = good

		if good.old_price:
			discount = calc_discount(good) 
		else:
			discount = None

		item.discount = discount

		main_images = Picture.objects.filter(good=good, main_image=True).first()

		images = Picture.objects.filter(good=good, main_image=False)
		
		item.main_images = main_images
		item.images = images

		 	
		table.append(item)

		context = {

			'catalog_table': table,

		}

		context.update(get_cart_header(request))

	return render(request, 'baseapp/index.html', context)
	

def send_price(request,  addr_to):

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	filepath = os.path.join(BASE_DIR, 'price')


	addr_from = "info@annasoft.ru"                                   
	password  = "M@sterkey$302"

	msg = MIMEMultipart()                               
	msg['From']    = addr_from                          
	msg['To']      = addr_to                            
	msg['Subject'] = 'Прайс лист компаниии ЭКВАДОРОЗА'
	                                    
	if os.path.isfile(filepath):
		filename = os.path.basename(filepath)
	elif os.path.exists(filepath):
		dir_ = os.listdir(filepath)
		for f in dir_:
			attach_file(msg,filepath+"/"+f)
			break


	body = "Текст сообщения"
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP('smtp.mail.ru', 25)                                  
	server.starttls()                                   
	server.login(addr_from, password)                 
	server.send_message(msg)                           
	server.quit()

def attach_file(msg, filepath):                             
    filename = os.path.basename(filepath)                   
    ctype, encoding = mimetypes.guess_type(filepath)        
    if ctype is None or encoding is not None:               
        ctype = 'application/octet-stream'                  
    maintype, subtype = ctype.split('/', 1)                 
    if maintype == 'text':                                  
        with open(filepath) as fp:                          
            file = MIMEText(fp.read(), _subtype=subtype)    
            fp.close()                                      
    elif maintype == 'image':                               
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':                               
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:                                                   
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)              
            file.set_payload(fp.read())                     
            fp.close()
            encoders.encode_base64(file)                    
    file.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(file)


def get_price(request):
	if request.method == 'POST':
		price_form = GetPriceForm(request.POST)
		if price_form.is_valid():


			userfirst_name 	= price_form.cleaned_data['userfirst_name']
			userlast_name 	= price_form.cleaned_data['userlast_name']
			companyname 	= price_form.cleaned_data['companyname']
			useremail 		= price_form.cleaned_data['useremail']
			usertel 		= price_form.cleaned_data['usertel']
			usercomment 	= price_form.cleaned_data['usercomment']

			new_buyer		= Buyer(first_name=userfirst_name, last_name=userlast_name, Phone=usertel, email=useremail)
			new_buyer.save()

			send_price(request, useremail)


			return render(request, 'baseapp/get_price.html')

		else:

			return redirect('show_index')