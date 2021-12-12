from django.shortcuts import render

from users.models import User

def index(request):
    context = {
        'users': User.objects.all(),
        'title': 'Administración de usuarios'
    }

    return render(request, 'users/index.html', context)