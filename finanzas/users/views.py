from django.shortcuts import render
from django.shortcuts import redirect

from users.models import User
from .forms import UserForm


def index(request):
    context = {
        'users': User.objects.all(),
        'title': 'Administración de usuarios'
    }

    return render(request, 'users/index.html', context)


def create(request):
    form =  UserForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect('users:index')
    
    context = {
        'title': 'Nuevo usuario',
        'form': form
    }
    
    return render(request, 'users/create.html', context)