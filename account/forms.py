
from django import forms
from .models import *
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')




class TradersDetailsForm(forms.ModelForm):

    phone = forms.CharField()
  
    class Meta:
        model = TradersDetails
        fields =('phone',) 

        Widget ={ 'phone':forms.TextInput(attrs={'class':'form-control'}) }
            





class TradersLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')       