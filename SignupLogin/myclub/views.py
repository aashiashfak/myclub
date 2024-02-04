from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products
# Create your views here.


@login_required(login_url='login')
def index(request):
    visits = int(request.COOKIES.get('visits',0))
    visits+=1
    username = request.user.username 
    items = Products.objects.all()
    context = {
        'username': username,
        'items':items, 
        'visits':visits
        }
    response = render(request, 'index.html', context)
    response.set_cookie('visits', visits)
    return response