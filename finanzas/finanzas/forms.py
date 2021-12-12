from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'username', 'placeholder': 'Username'
    }))

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'id': 'password', 'placeholder': 'Password'
    }))