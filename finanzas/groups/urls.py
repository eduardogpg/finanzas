from django.urls import path
from django.urls import include

from .views import create
from .views import GroupListView

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='list'),
    path('crear/', create, name='create'),

    path('<int:group_pk>/creditos/', include('credits.urls')),
]
