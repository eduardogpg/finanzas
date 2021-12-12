from django.shortcuts import render
from django.shortcuts import redirect

from prospects.models import Client

def dashboard(request):
    context = {
        'title' :'Finanzas del sur',
        'clients': Client.objects.all()
    }
    return render(request, 'index.html', context)

def index(request):
    return redirect('dashboard')
    