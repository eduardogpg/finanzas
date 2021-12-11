from django import forms
from django.core.exceptions import ValidationError


class NewCreditForm(forms.Form):
    error_css_class = "text-red-600"
    
    name = forms.CharField(label='Nombre(s)', max_length=100, required=True)
    last_name = forms.CharField(label='Apellidos', max_length=100, required=True)
    curp = forms.CharField(label='CURP', max_length=18, required=True)
    dni = forms.CharField(label='Clave de elector', max_length=18, required=True)
    phone_number = forms.CharField(label='Número teléfonico', max_length=10, required=True)
    
    def __init__(self, *args, **kwargs):
        super(NewCreditForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['class'] = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
        self.fields['last_name'].widget.attrs['class'] = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
        self.fields['curp'].widget.attrs['class'] = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
        self.fields['dni'].widget.attrs['class'] = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
        self.fields['phone_number'].widget.attrs['class'] = 'block w-full px4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
        
        
    
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        
        if data.isnumeric():
            return data

        raise ValidationError('El número teléfonico debe contener unicamente números.')
    
    
    def clean_curp(self):
        data = self.cleaned_data['curp']
        
        if len(data) == 18:
            return data

        raise ValidationError('La CURP debe poseer 18 caracteres.')
    

    def clean_dni(self):
        data = self.cleaned_data['dni']
        
        if len(data) == 18:
            return data

        raise ValidationError('La clave de elector debe poseer 18 caracteres.')
    
    