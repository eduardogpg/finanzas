from django.shortcuts import render

from django.shortcuts import get_object_or_404

from prospects.models import Client
from prospects.models import Prospect

def index(request):
    client = None
    
    if request.method == 'GET' and request.GET.get('curp'):
        prospect = Prospect.objects.filter(curp=request.GET['curp']).first()
        
        if prospect and prospect.client:
            client = prospect.client

    return render(request, 'clients/index.html', {
        'title': 'Busqueda de clientes',
        'client': client
    })


def detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    return render(request, 'clients/detail.html', {
        'client': client
    })