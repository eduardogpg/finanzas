from django.urls import path
from django.urls import include

from .views import create
from .views import GroupListView
from .views import GroupDetailView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('detalles/<int:pk>', GroupDetailView.as_view(), name='detail'),
    
    path('crear/', create, name='create'),
    path('<int:group_pk>/creditos/', include('credits.urls')),
]
