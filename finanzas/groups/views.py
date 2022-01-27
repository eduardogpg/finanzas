import json

from django.urls import reverse

from django.shortcuts import get_object_or_404

from django.http import JsonResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.decorators.csrf import csrf_exempt

from .models import Group
from folders.models import Folder

class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'

    def dispatch(self, request, *args, **kwargs):
        self.folder_pk = kwargs.get('pk')
        self.folder = get_object_or_404(Folder, pk=self.folder_pk)
        
        return super(GroupListView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['folder'] = self.folder
        context['groups'] = self.object_list
        
        return context
    
    
    def get_queryset(self):
        return self.folder.groups.all().order_by('-id')


class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

@csrf_exempt
def create(request, pk):
    
    response = dict()
    body = json.loads(request.body.decode('utf-8'))
    
    
    if request.method == 'POST' and body.get('name') and body.get('folder_id'):
        folder = get_object_or_404(Folder, pk=body['folder_id'])
        group = Group.objects.create(name=body['name'], folder=folder) 
        
        response['id'] = group.id
        response['name'] = group.name
        response['folder_id'] = folder.id
        
        response['next_url'] = reverse('folders:groups:list', kwargs={'pk':folder.pk})
        
    return JsonResponse(response)