import json

from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt

from .models import Folder

class FolderListView(ListView):
    model = Folder
    template_name = 'folders/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

@csrf_exempt
def create(request):
    response = dict()
    body = json.loads(request.body.decode('utf-8'))
    
    if request.method == 'POST' and body.get('name'):
        folder = Folder.objects.create(name=body['name']) 
        
        response['id'] = folder.id
        response['name'] = folder.name
        
    return JsonResponse(response)