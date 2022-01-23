from django.urls import path
from django.urls import include

from .views import create
from .views import FolderListView


app_name = 'folders'

urlpatterns = [
    path('', FolderListView.as_view(), name='list'),
    path('create', create, name='create'),
    
    path('<int:pk>/grupos', include('groups.urls')),
]
