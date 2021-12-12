from .views import index
from django.urls import path

from .views import index
from .views import create, update

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', create, name='create'),
    path('<int:pk>/actualizar/', update, name='update'),
]
