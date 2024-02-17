from django.shortcuts import redirect
from django.contrib import messages
class RestrictNormalUserFromAdminPanel:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for the admin panel and the user is a regular user
        if request.path.startswith('/admin/') and not request.user.is_superuser and request.user.is_authenticated:
            # Redirect regular users away from the admin panel and send a error message 
            messages.error(request, "This page is not accessible for you")
            return redirect('index')

        response = self.get_response(request)
        return response

class RestrictAdminFromFrontend:
        def __init__(self,get_response):
            self.get_response = get_response

        def __call__(self, request):
            if request.user.is_authenticated and request.user.is_superuser and request.path.startswith('/myclub/index'):
                return redirect('login')
            
            response = self.get_response(request)
            return response