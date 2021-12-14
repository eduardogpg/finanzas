from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

from users.models import User
from .forms import UserForm

from .decorators import only_admins

@only_admins
def index(request):
    context = {
        'users': User.objects.all(),
        'title': 'Administración de usuarios'
    }

    return render(request, 'users/index.html', context)

@only_admins
def create(request):
    form =  UserForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            active=form.cleaned_data['active'],
            is_superuser=form.cleaned_data['is_superuser']
        )
        
        return redirect('users:index')
    
    context = {
        'title': 'Nuevo usuario',
        'form': form
    }
    
    return render(request, 'users/create.html', context)

@only_admins
def update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(initial={
        'username': user.username, 'email': user.email, 'active': user.active, 'is_superuser': user.is_superuser 
    })
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            
            user.username = form.cleaned_data['username']
            user.active = form.cleaned_data['active']
            user.is_superuser = form.cleaned_data['is_superuser']
            
            user.save()
            
        return redirect('users:index')
    
    context = {
        'title': 'Nuevo usuario',
        'form': form,
        'user': user
    }
    
    return render(request, 'users/update.html', context)