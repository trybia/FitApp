from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View, CreateView
from .forms import *
# Create your views here.
#tworzenie użytkownika i logowanie
class UserFormView(View):
    form_class = UserForm
    template_name = 'index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})


def showMyHome(request):
    return render(request, 'home.html')

#wylogowanie
def logout_view(request):
    logout(request)
    return redirect('home')

#logowanie
class ShowLoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'index.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'home.html')
            else:
                return HttpResponse('Nie udało się zalogować')


def thanks(request):
    return HttpResponse('Dziekujemy za wypełnienie formularza')

class NewUserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'index.html'
    success_url = reverse_lazy ('home')

class AddUserProfileView(generic.View):
    model = UserProfile
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            form = AddUserProfileForm
            return render(request, 'index.html', {'form':form})
        else:
            return redirect('/login')
    def post(self, request):
        user = User.objects.get(request.user.id)
        form = AddUserProfileForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse('Formularz został wypełniony.')
        else:
            return render(request, 'index.html', {'form':form})


