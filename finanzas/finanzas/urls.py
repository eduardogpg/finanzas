
from django.contrib import admin
from django.urls import path, include

from .views import index
from .views import dashboard

from .views import login
from .views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('login', login, name='login'),
    path('logout', logout, name='logout'),

    path('dashboard', dashboard, name='dashboard'), 
    path('creditos/', include('credits.urls')),
    path('clientes/', include('clients.urls')),
    path('usuarios/', include('users.urls')),
]
