from django.shortcuts import redirect

def only_admins(function):
    def wrapper(request, *args, **kwargs):
        
        if not request.user.is_superuser:
            return redirect('dashboard')
        
        return function(request, *args, **kwargs)
    
    return wrapper