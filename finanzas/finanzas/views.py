from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from prospects.models import Client

from .forms import LoginForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    context = {
        'title' :'Finanzas del sur',
        'clients': Client.objects.all()
    }
    return redirect('folders:list')

    # return render(request, 'index.html', context)


def index(request):
    return redirect('dashboard')


def login(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            username=form.data['username'],
            password=form.data['password']
        )
        
        if user and user.active:
            django_login(request, user)
            user.authenticate_now()
            
            return redirect('dashboard')
    
    if request.method == 'POST':
        messages.error(request, 'Usuario o contraseña incorrectos')
    
    context = { 'title': 'Login', 'form': form }
    return render(request, 'login.html', context)



def logout(request):
    django_logout(request)
    return redirect('login')