from django.urls import path

from .views import filter
from .views import create

app_name = 'credits'

urlpatterns = [
    path('nuevo/', create, name='create'),
    path('filter', filter, name='filter'),
]
