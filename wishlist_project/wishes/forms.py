from django import forms
from django.contrib.auth.models import User
from .models import Wish, List

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        exclude = ['list','is_purchased']

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        exclude = ['creator','id']
