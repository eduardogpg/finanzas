
from django.contrib import admin
from django.urls import path, include

from .views import index
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('dashboard', dashboard, name='dashboard'), 
    path('creditos/', include('credits.urls'))
]
