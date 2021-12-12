from django import forms
from django.core.exceptions import ValidationError

from prospects.models import Client
from addresses.models import STATES_CHOICES

DNI_LENGHT = 18

class NewCreditForm(forms.Form):
    
    input_text_css = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
    select_input_css = 'appearance-none block w-full px-4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
    
    request_amount = forms.CharField(label='Credito Solicitado', max_length=10, required=True, initial=0)
    authorized_amount = forms.CharField(label='Credito Autorizado', max_length=10, required=True, initial=0)
    
    name = forms.CharField(label='Nombre(s)', max_length=100, required=True)
    last_name = forms.CharField(label='Apellidos', max_length=100, required=True)
    curp = forms.CharField(label='CURP', max_length=18, required=True)
    dni = forms.CharField(label='Clave de elector', max_length=DNI_LENGHT, required=True)
    phone_number = forms.CharField(label='Número teléfonico', max_length=10, required=True)
    
    address = forms.CharField(label='Domicilio (Calle, número)', max_length=100, required=True)
    state = forms.ChoiceField(label='Estado', choices=STATES_CHOICES, required=True)
    township = forms.CharField(label='Ciudad', max_length=100, required=True)
    suburb = forms.CharField(label='Colonia', max_length=100, required=True)
    zip = forms.CharField(label='Código Postal', max_length=10, required=True)
    
    lat = forms.CharField(label='Latitúd', max_length=10, required=True)
    long = forms.CharField(label='Longitud', max_length=10, required=True)
    
    marital_state = forms.ChoiceField(label='Estado Civil', choices=Client.MARITAL_STATE_CHOICES.choices, required=True)
    spouse = forms.CharField(label='Nombre del conyugue', max_length=200, required=False)
    job = forms.CharField(label='Ocupación', max_length=200, required=True)
    children = forms.IntegerField(label='Número de hijos', required=True, initial=0)
    
    aval_name = forms.CharField(label='Nombre(s)', max_length=100, required=True)
    aval_last_name = forms.CharField(label='Apellidos', max_length=100, required=True)
    aval_curp = forms.CharField(label='CURP', max_length=18, required=True)
    aval_dni = forms.CharField(label='Clave de elector', max_length=DNI_LENGHT, required=True)
    aval_phone_number = forms.CharField(label='Número teléfonico', max_length=10, required=True)
    
    aval_address = forms.CharField(label='Domicilio (Calle, número)', max_length=100, required=True)
    aval_state = forms.ChoiceField(label='Estado', choices=STATES_CHOICES, required=True)
    aval_township = forms.CharField(label='Ciudad', max_length=100, required=True)
    aval_suburb = forms.CharField(label='Colonia', max_length=100, required=True)
    aval_zip = forms.CharField(label='Código Postal', max_length=10, required=True)
    
    
    reference_1_name = forms.CharField(label='Nombre', max_length=100, required=True)
    reference_1_contact = forms.CharField(label='Contacto', max_length=255, required=True)
    reference_1_address = forms.CharField(label='Dirección', max_length=18, required=True)
    reference_1_relationship = forms.CharField(label='Parentesco', max_length=100, required=True)
    
    reference_2_name = forms.CharField(label='Nombre', max_length=200, required=True)
    reference_2_contact = forms.CharField(label='Contacto', max_length=255, required=True)
    reference_2_address = forms.CharField(label='Dirección', max_length=28, required=True)
    reference_2_relationship = forms.CharField(label='Parentesco', max_length=100, required=True)
    
    guarantee_1 = forms.CharField(label='Artículo 1 (Descripción)', required=True, widget=forms.Textarea(
        attrs={'rows':4 }
    ))
    
    guarantee_2 = forms.CharField(label='Artículo 2 (Descripción)', required=True, widget=forms.Textarea(
        attrs={'rows':4 }
    ))
    
    guarantee_3 = forms.CharField(label='Artículo 3 (Descripción)', required=True, widget=forms.Textarea(
        attrs={'rows':4 }
    ))
    
    
    def __init__(self, *args, **kwargs):
        super(NewCreditForm, self).__init__(*args, **kwargs)

        self.fields['request_amount'].widget.attrs['class'] = self.input_text_css
        self.fields['authorized_amount'].widget.attrs['class'] = self.input_text_css
        
        self.fields['name'].widget.attrs['class'] = self.input_text_css
        self.fields['last_name'].widget.attrs['class'] = self.input_text_css
        self.fields['curp'].widget.attrs['class'] = self.input_text_css
        self.fields['dni'].widget.attrs['class'] = self.input_text_css
        self.fields['phone_number'].widget.attrs['class'] = self.input_text_css
        
        self.fields['address'].widget.attrs['class'] = self.input_text_css
        self.fields['state'].widget.attrs['class'] = self.select_input_css
        self.fields['township'].widget.attrs['class'] = self.input_text_css
        self.fields['suburb'].widget.attrs['class'] = self.input_text_css
        self.fields['zip'].widget.attrs['class'] = self.input_text_css
        
        self.fields['lat'].widget.attrs['class'] = self.input_text_css
        self.fields['long'].widget.attrs['class'] = self.input_text_css
        
        self.fields['marital_state'].widget.attrs['class'] = self.input_text_css
        self.fields['spouse'].widget.attrs['class'] = self.select_input_css
        self.fields['job'].widget.attrs['class'] = self.input_text_css
        self.fields['children'].widget.attrs['class'] = self.input_text_css
        
        self.fields['aval_name'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_last_name'].widget.attrs['class'] = self.select_input_css
        self.fields['aval_curp'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_dni'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_phone_number'].widget.attrs['class'] = self.input_text_css
        
        self.fields['aval_address'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_state'].widget.attrs['class'] = self.select_input_css
        self.fields['aval_township'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_suburb'].widget.attrs['class'] = self.input_text_css
        self.fields['aval_zip'].widget.attrs['class'] = self.input_text_css
        
        
        self.fields['reference_1_name'].widget.attrs['class'] = self.input_text_css
        self.fields['reference_1_contact'].widget.attrs['class'] = self.select_input_css
        self.fields['reference_1_address'].widget.attrs['class'] = self.input_text_css
        self.fields['reference_1_relationship'].widget.attrs['class'] = self.input_text_css
        
        self.fields['reference_2_name'].widget.attrs['class'] = self.input_text_css
        self.fields['reference_2_contact'].widget.attrs['class'] = self.select_input_css
        self.fields['reference_2_address'].widget.attrs['class'] = self.input_text_css
        self.fields['reference_2_relationship'].widget.attrs['class'] = self.input_text_css
        
        self.fields['guarantee_1'].widget.attrs['class'] = self.input_text_css
        self.fields['guarantee_2'].widget.attrs['class'] = self.input_text_css
        self.fields['guarantee_3'].widget.attrs['class'] = self.input_text_css
        
    
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        return self.phone_number_validator(data)
    
    
    def clean_curp(self):
        data = self.cleaned_data['curp']
        return self.curp_validator(data)
    
    
    def clean_dni(self):
        data = self.cleaned_data['dni']
        return self.dni_validator(data)
    
    
    def clean_aval_phone_number(self):
        data = self.cleaned_data['aval_phone_number']
        return self.phone_number_validator(data)
    
    
    def clean_aval_curp(self):
        data = self.cleaned_data['aval_curp']
        return self.curp_validator(data)
    
    
    def clean_avala_dni(self):
        data = self.cleaned_data['avala_dni']
        return self.dni_validator(data)
    
    
    # Validacón para el CURP!
    
    
    # ------- Validators -------
    
    def dni_validator(self, dni):
        if len(dni) == DNI_LENGHT:
            return dni

        raise ValidationError('La clave de elector debe poseer 18 caracteres.')
    
    
    def curp_validator(self, curp):
        if len(curp) == 18:
            return curp

        raise ValidationError('La CURP debe poseer 18 caracteres.')
    
    
    def phone_number_validator(self, phone_number):
        
        if not phone_number.isnumeric():
            raise ValidationError('El número teléfonico debe contener unicamente números.')
        
        if not len(phone_number) == 10:
            raise ValidationError('El número teléfonico debe ser a 10 dígitos.')

        return phone_number
        