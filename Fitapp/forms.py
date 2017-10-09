from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Fitapp.models import UserProfile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','type',)
        # https://stackoverflow.com/questions/16356289/how-to-show-datepicker-calender-on-datefield
        widgets = {
            'age': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class ManagerProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

