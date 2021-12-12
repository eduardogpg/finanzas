from django.db import transaction

from django.shortcuts import render
from django.shortcuts import redirect

from .forms import NewCreditForm

from credits.models import Credit
from addresses.models import Address

from prospects.models import Aval
from prospects.models import Client
from prospects.models import Prospect
from prospects.models import Reference

from guarantees.models import Guarantee

def clean_reference(form, reference):
    return {
        'name': form.cleaned_data[f'{reference}_name'],
        'address': form.cleaned_data[f'{reference}_address'],
        'contact': form.cleaned_data[f'{reference}_contact'],
        'relationship':form.cleaned_data[f'{reference}_relationship'],
    }

def create_entities(form):
    prospect = Prospect(
        name=form.cleaned_data['name'],
        last_name=form.cleaned_data['last_name'],
        phone_number=form.cleaned_data['phone_number'],
        curp=form.cleaned_data['curp'],
        DNI=form.cleaned_data['dni'],
    )
    
    with transaction.atomic():
        prospect.save()

        client = Client.objects.create(
            prospect=prospect,
            job=form.cleaned_data['job'],
            spouse=form.cleaned_data['spouse'],
            children=form.cleaned_data['children'],
            marital_state=form.cleaned_data['marital_state'],
        )
        
        Address.objects.create(
            address=form.cleaned_data['address'],
            zip=form.cleaned_data['zip'],
            state=form.cleaned_data['state'],
            suburb=form.cleaned_data['suburb'],
            township=form.cleaned_data['township'],
            lat=form.cleaned_data['lat'],
            long=form.cleaned_data['long'],
            prospect=prospect
        )

        Credit.objects.create(
            client=client,
            request_amount=form.cleaned_data['request_amount'],
            authorized_amount=form.cleaned_data['authorized_amount']
        )

        # Aval
        prospect_aval = Prospect.objects.create(
            name=form.cleaned_data['aval_name'],
            last_name=form.cleaned_data['aval_last_name'],
            phone_number=form.cleaned_data['aval_phone_number'],
            curp=form.cleaned_data['aval_curp'],
            DNI=form.cleaned_data['aval_dni'],
        )
        
        Address.objects.create(
            prospect=prospect_aval, 
            address=form.cleaned_data['aval_address'],
            zip=form.cleaned_data['aval_zip'],
            state=form.cleaned_data['aval_state'],
            suburb=form.cleaned_data['aval_suburb'],
            township=form.cleaned_data['aval_township']
        )
        
        Aval.objects.create(prospect=prospect_aval, client=client)
        
        # Referencias
        Reference.objects.create_reference(client, clean_reference(form, 'reference_1'))
        Reference.objects.create_reference(client, clean_reference(form, 'reference_2'))
        
        # Garantias
        Guarantee.objects.create(client=client, description=form.cleaned_data['guarantee_1'])
        Guarantee.objects.create(client=client, description=form.cleaned_data['guarantee_2'])
        Guarantee.objects.create(client=client, description=form.cleaned_data['guarantee_3'])
        
        return client
    

def create(request):
    form = NewCreditForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        if create_entities(form):
            return redirect('index')
    

    return render(request, 'credits/create.html', {
        'form': form,
        'title':'Nuevo credito'
    })