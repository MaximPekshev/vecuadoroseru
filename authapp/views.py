from django.shortcuts 				import render, redirect

from django.http 					import HttpResponse
from django.http 					import HttpResponseRedirect

from django.contrib.auth.models		import User
from django.contrib.auth.forms 		import AuthenticationForm
from django.contrib.auth.forms 		import UserCreationForm
from django.contrib					import messages

from django.views.generic.edit 		import FormView
from django.contrib		 			import auth
from cartapp.views 					import get_cart_header
from .forms 						import RegistrationForm
from authapp.models 				import Buyer
from baseapp.forms 					import GetPriceForm


def show_account(request):



	context = {

	}

	template_name = 'authapp/my-account.html'

	context.update( get_cart_header(request))

	buyer = Buyer.objects.filter(user=request.user).first()
	
	if buyer is not None:
		
		context.update({'buyer': buyer})

	return render(request, template_name, context)


def login_register(request):

	context = {
		}

	if request.GET.get('login'):
		context = {
		'login_true':True,
		}

	context.update(get_cart_header(request))	

	template_name = 'authapp/login-register.html'
	
	return render(request, template_name, context)


def login(request):

	if request.method == 'POST':
		form 				= AuthenticationForm(request, request.POST)

		username 		= form.data.get('username')
		password 		= form.data.get('password')

		user 			= auth.authenticate(username=username, password=password)

		if user is not None:

			auth.login(request, user)

			return redirect('show_account')

		else:
			context = {
				'login_true':True,
				}

			context.update(get_cart_header(request))

			messages.info(request, 'Комбинации пароль-логин не существует!')

			return render(request, 'authapp/login-register.html', context)
	
	return HttpResponseRedirect('/')


def logout(request):

	context = {
		'login_true':True,
		}
	

	auth.logout(request)

	context.update(get_cart_header(request))

	return render(request, 'authapp/login-register.html', context)


def register(request):

	if request.method == 'POST':

		reg_form = RegistrationForm(request.POST)

		if reg_form.is_valid():

			userfirst_name 	= reg_form.cleaned_data['userfirst_name']
			userlast_name 	= reg_form.cleaned_data['userlast_name']
			companyname 	= reg_form.cleaned_data['companyname']
			usertel 		= reg_form.cleaned_data['usertel']
			username 		= reg_form.cleaned_data['username']
			useremail 		= reg_form.cleaned_data['useremail']
			userpassword 	= reg_form.cleaned_data['userpassword']
			userpassword_2 	= reg_form.cleaned_data['userpassword_2']

			if userpassword==userpassword_2:
				if User.objects.filter(username=username).exists():
					messages.info(request, 'Пользователь с таким именем существует!!!')
					return redirect('login_register')
				elif User.objects.filter(email=useremail).exists():				
					messages.info(request, 'Пользователь с таким email существует!!!')
					return redirect('login_register')
				else:
					user = User.objects.create_user(username=username, password=userpassword, email=useremail)
					user.save()

					new_buyer		= Buyer(user=user, first_name=userfirst_name, last_name=userlast_name, Phone=usertel, email=useremail, name=companyname)
					new_buyer.save()

					auth.login(request, user)

					template_name = 'authapp/my-account.html'

					return render(request, template_name, get_cart_header(request))	
			else:
				messages.info(request, 'Пароли не совпадают!!!')
				return redirect('login_register')			

	else:


		return redirect('login_register')


def change_password(request):

	return redirect('show_index')

def save_profile(request):

	if request.method == 'POST':
		form = GetPriceForm(request.POST)

		if form.is_valid():

			userfirst_name 	= form.cleaned_data['userfirst_name']
			userlast_name 	= form.cleaned_data['userlast_name']
			companyname 	= form.cleaned_data['companyname']
			usertel 		= form.cleaned_data['usertel']
			useremail 		= form.cleaned_data['useremail']

			user = User.objects.get(username = request.user.username)
			if user is not None:
				buyer = Buyer.objects.get(user = user)
				if buyer is not None:
					return HttpResponse('{}{}'.format(user, buyer))

		else:
			return HttpResponse('Проблема с формой')
	else:				
		return HttpResponse('Не работает')				