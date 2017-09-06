from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, CreateView

from .forms import *
# Create your views here.

#tworzenie użytkownika i logowanie
class UserFormView(View):

    def get(self, request):
        form = UserForm
        return render(request, 'useradd.html', {'form':form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        else:
            return render(request, 'useradd.html', {'form':form})



def MyHome(request):
    return render(request, 'index.html')

# #wylogowanie
# def logout_view(request):
#     logout(request)
#     return redirect('home')

#logowanie
class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'useradd.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                return HttpResponse('Nie udało się zalogować')



class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'useradd.html'
    success_url = reverse_lazy ('home')


#dodawanie profilu do utworzonego użytkownika
@login_required
#@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        if request.user.userprofile.type == 100:
            profile_form = ManagerProfileForm(request.POST, instance=request.user.userprofile)
        else:
            profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
        else:
            messages.error(request, ('Proszę poprawić bląd.'))
    else:

        if request.user.userprofile.type == 100:
            profile_form = ManagerProfileForm(instance=request.user.userprofile)
        else:
            profile_form = UserProfileForm(instance=request.user.userprofile)

        return render(request, 'updateprofile.html', {
        'profile_form': profile_form

    })

