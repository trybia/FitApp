from django.contrib.auth import authenticate, login, models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import View, CreateView


from .forms import *
# Create your views here.

#tworzenie użytkownika
class UserFormView(View):

    def get(self, request):
        form = UserForm
        return render(request, 'Fitapp/useradd.html', {'form':form})

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
            return render(request, 'Fitapp/useradd.html', {'form':form})



def MyHome(request):
    return render(request, 'Fitapp/index.html')

#logowanie
class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'Fitapp/useradd.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'Fitapp/index.html')
            else:
                return HttpResponse('Nie udało się zalogować')



class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'Fitapp/useradd.html'
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
            return redirect('/')
        else:
            messages.error(request, ('Proszę poprawić bląd.'))
    else:

        if request.user.userprofile.type == 100:
            profile_form = ManagerProfileForm(instance=request.user.userprofile)
        else:
            profile_form = UserProfileForm(instance=request.user.userprofile)

        return render(request, 'Fitapp/updateprofile.html', {
        'profile_form': profile_form})

@login_required
#@transaction.atomic
def manage_clients(request):
    if request.GET.get('delete'):
        #nieskończona opcja kasowania relacji trener-klient
        id = request.GET.get('delete')
        return redirect('/clients')
    else:

        #https://stackoverflow.com/questions/41061706/django-query-filter-by-user-group
        clients_list = User.objects.filter(groups__name='clients')

        # z dokumentacji: https://docs.djangoproject.com/en/1.11/topics/pagination/
        paginator = Paginator(clients_list,25)

        page = request.GET.get('page')
        try:
            clients = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            clients = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            clients = paginator.page(paginator.num_pages)
        return render(request, 'Fitapp/clients.html', {'clients': clients})

@login_required
#@transaction.atomic
def manage_coaches(request):
    if request.GET.get('delete'):
        #nieskończona opcja kasowania relacji trener-klient
        id = request.GET.get('delete')
        return redirect('/coaches')
    else:

        #https://stackoverflow.com/questions/41061706/django-query-filter-by-user-group
        coaches_list = User.objects.filter(groups__name='coaches')

        # z dokumentacji: https://docs.djangoproject.com/en/1.11/topics/pagination/
        paginator = Paginator(coaches_list,25)

        page = request.GET.get('page')
        try:
            coaches = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            coaches = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            coaches = paginator.page(paginator.num_pages)
        return render(request, 'Fitapp/coaches.html', {'coaches': coaches})

@login_required
#@transaction.atomic
def manage_dieticians(request):
    if request.GET.get('delete'):
        #nieskończona opcja kasowania relacji trener-klient
        id = request.GET.get('delete')
        return redirect('/dieticians')
    else:

        #https://stackoverflow.com/questions/41061706/django-query-filter-by-user-group
        dieticians_list = User.objects.filter(groups__name='dieticians')

        # z dokumentacji: https://docs.djangoproject.com/en/1.11/topics/pagination/
        paginator = Paginator(dieticians_list,25)

        page = request.GET.get('page')
        try:
            dieticians = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            dieticians = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            dieticians = paginator.page(paginator.num_pages)
        return render(request, 'Fitapp/dieticians.html', {'dieticians': dieticians})

