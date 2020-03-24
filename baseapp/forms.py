from django import forms
 
class GetPriceForm(forms.Form):
	userfirst_name  = forms.CharField(max_length = 50)
	userlast_name  	= forms.CharField(max_length = 50)
	companyname = forms.CharField(max_length = 50, required=False)
	useremail = forms.EmailField(max_length=254)
	usertel	= forms.CharField(max_length = 50)
	usercomment = forms.CharField(max_length = 50, required=False)