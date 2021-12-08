from django.shortcuts import render

def create(request):
    context = {}
    return render(request, 'credits/create.html', context)