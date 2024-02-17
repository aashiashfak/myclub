from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def home_page(request):
    """
    Render the home page.
    Redirect to 'index' if the user is already logged in.
    """
    if 'username' in request.session:
        return redirect('index')
   
    return render(request, 'home.html')


@never_cache
def signup(request):
    """
    Handle user signup.
    Redirect to 'index' if the user is already logged in.
    """
    form = CreateUserForm()

    if 'username' in request.session:
        return redirect('index')
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {'signupform': form}
    return render(request, 'signup.html', context)


@never_cache
def user_login(request):
    """
    Handle user login. If user is authenticated store username in session.
    Redirect to 'index' if the user is already logged in.
    """
    if 'username' in request.session:
        return redirect('index')
    
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['username'] = username
                login(request, user)

                return redirect('myclub/index')
                
    context = {'loginform': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def user_logout(request):
    """
    Handle user logout and delete the cookie.
    Log the user out and redirect to 'home'.
    """
    logout(request)
    response = redirect('home')
    response.delete_cookie('visits')
    return response
