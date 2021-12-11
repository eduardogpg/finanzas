from django.db import transaction

from django.shortcuts import render

from .forms import NewCreditForm

from prospects.models import Aval
from prospects.models import Client
from prospects.models import Prospect


def create_entities(form):
    prospect = Prospect(
        name=form.cleaned_data['name'],
        last_name=form.cleaned_data['last_name'],
        phone_number=form.cleaned_data['phone_number'],
        curp=form.cleaned_data['curp'],
        DNI=form.cleaned_data['DNI'],
    )
    
    with transaction.atomic():
        prospect.save()
        client = Client.objects.create(prospect=prospect)

        return client
    

def create(request):
    form = NewCreditForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        client = create_entities(form)
        
        return redirect('index')
    
    
    return render(request, 'credits/create.html', {
        'form': form
    })