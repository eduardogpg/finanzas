from django.urls import path

from .views import search
from .views import create
from .views import detail

from .views import index

app_name = 'credits'

urlpatterns = [
    path('', index, name='index'),
    
    path('nuevo/', create, name='create'),
    path('search', search, name='search'),
    
    path('detalle/<int:pk>', detail, name='detail'),
]
