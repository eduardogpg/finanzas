from django.shortcuts import render
from django.shortcuts import redirect

def dashboard(request):
    context = {}
    return render(request, 'index.html', context)

def index(request):
    return redirect('dashboard')
    