from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Products
# from django.views.decorators.cache import cache_page

# Create your views here.

def get_product_list():
    """
    Fetches the products either from the cache or the database,
    and caches the result with a timeout if not already in the cache.
    """
    product_list = cache.get('product_list')

    if product_list is None:
        product_list = (Products.objects.all())
        cache.set('product_list', product_list, timeout=60)
        print("Fetched from database and cached.")
    else:
        print("Fetched from cache.")

    return product_list

# @cache_page(timeout=60*1) -if u need to cache the entire page
@login_required(login_url='login')
def index(request):
    """
    Renders the 'index.html' template with user-specific data,
    including the product list and visit count.
    """
    visits = int(request.COOKIES.get('visits',0))
    visits+=1
    username = request.user.username 
    Product_list = get_product_list()
    context = {
        'username': username,
        'product_list':Product_list, 
        'visits':visits
        }
    response = render(request, 'index.html', context)
    response.set_cookie('visits', visits)
    return response



