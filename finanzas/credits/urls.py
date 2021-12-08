from django.urls import path

from .views import create

app_name = 'credits'

urlpatterns = [
    path('create/', create, name='create'),
]
