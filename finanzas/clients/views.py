from django.shortcuts import render

from django.shortcuts import get_object_or_404

from prospects.models import Client
from prospects.models import Prospect

def index(request):
    context = { 'title': 'Busqueda de clientes' }
    
    if request.method == 'GET' and request.GET.get('curp'):
        client = Client.objects.filter(prospect__curp=request.GET['curp']).first()
        
        if client and client.credit:
            context['client'] = client

    return render(request, 'clients/index.html', context)
            

def detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    return render(request, 'clients/detail.html', {
        'client': client,
    })