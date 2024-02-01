from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Products



# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def signup(request):

    if 'username' in request.session:
        return redirect('index') 

    form = CreateUserForm()

    if request.method == 'POST':  
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')  
    
    context = {'signupform': form}  
    return render(request, 'signup.html', context)

def userlogin(request):

    if 'username' in request.session:
        return redirect('index') 
    
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username, password=password)
            
            if user is not None:
                request.session['username'] = username

                auth_login(request, user)
                return redirect('index')
        
    context = {'loginform': form}
    return render(request, 'login.html',context)

# @login_required(login_url='login')
def index(request):
    visits = int(request.COOKIES.get('visits',0))
    visits+=1
    username = request.user.username 
    items = Products.objects.all()
    context = {'username': username,
              'items':items, 
              'visits':visits}
    response = render(request, 'index.html', context)
    response.set_cookie('visits', visits)
    return response
    

def userlogout(request):
    auth_logout(request)

    return redirect('home')
    
    # response = HttpResponseRedirect('home.html')

    
    # response.delete_cookie('visits')
    
    # return response