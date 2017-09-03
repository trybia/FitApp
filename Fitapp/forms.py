from django import forms
from django.contrib.auth.models import User

from Fitapp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)

class AddUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
