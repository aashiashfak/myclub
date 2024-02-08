from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required


def home_page(request):
    """
    Render the home page.
    """
    if 'username' in request.session:
        return redirect('index')
   
    return render(request, 'home.html')


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


def user_login(request):
    """
    Handle user login.
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
            else:
                # Authentication failed, add a custom error to the form
                form.add_error(None, 'Invalid username or password')  # General error for the entire form
                form.add_error('username', 'Invalid username or password')
                form.add_error('password', 'Invalid username or password')
                print(form.errors)
                
    context = {'loginform': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def user_logout(request):
    """
    Handle user logout.
    Log the user out and redirect to 'home'.
    """
    logout(request)
    response = redirect('home')
    response.delete_cookie('visits')
    return response
