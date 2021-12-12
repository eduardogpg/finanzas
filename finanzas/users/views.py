from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

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


def update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form =  UserForm(instance=user)
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']
            user.is_active = form.cleaned_data['is_active']
            user.is_superuser = form.cleaned_data['is_superuser']
            
            user.save()
            
            return redirect('users:index')
    
    context = {
        'title': 'Nuevo usuario',
        'form': form,
        'user': user
    }
    
    return render(request, 'users/update.html', context)