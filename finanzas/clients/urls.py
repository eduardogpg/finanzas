from django.urls import path

from .views import index
from .views import detail

app_name = 'clients'

urlpatterns = [
    path('', index, name='index'),
    path('detalles/<int:pk>', detail, name='detail'),
]
