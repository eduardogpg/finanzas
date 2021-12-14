from django import forms
from .models import User

class UserForm(forms.Form):
    select_input_css = 'appearance-none block w-full px-4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
    
    username = forms.CharField(
        min_length=4, max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'username'
    }))
    
    email = forms.CharField(
        min_length=4, max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'email'
    }))

    password = forms.CharField(
        label='Password',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'id': 'password'
    }))
    
    active = forms.BooleanField(initial=True, required=False)
    is_superuser = forms.BooleanField(initial=True, required=False)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = self.select_input_css
        self.fields['email'].widget.attrs['class'] = self.select_input_css
        self.fields['password'].widget.attrs['class'] = self.select_input_css
        
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['password'].label = "Password"
        
        self.fields['active'].label = "Estatus activo"
        self.fields['is_superuser'].label = "Administrador" # Tipos

