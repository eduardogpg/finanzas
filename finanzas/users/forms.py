from django.forms import ModelForm
from django.forms import TextInput

from .models import User

class UserForm(ModelForm):
    select_input_css = 'appearance-none block w-full px-4 py-3 mb-2 text-sm placeholder-gray-500 bg-white border rounded'
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_active', 'is_superuser')
        widgets={
            'password':TextInput(attrs={'type':'password'})
        }
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = self.select_input_css
        self.fields['email'].widget.attrs['class'] = self.select_input_css
        self.fields['password'].widget.attrs['class'] = self.select_input_css
        
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['password'].label = "Password"
        
        self.fields['is_active'].label = "Activo"
        self.fields['is_superuser'].label = "Administrador"