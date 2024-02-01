from django.urls import path
from . import views

urlpatterns = [

    path('',views.home_page,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.userlogin,name='login'),
    path('index',views.index,name='index'),
    path('logout',views.userlogout,name='logout')

]
