from django.urls import path

from .views import create

app_name = 'credits'

urlpatterns = [
    path('nuevo/', create, name='create'),
]
