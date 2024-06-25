from django.contrib import admin
from django.urls import path, include
from .views import home, calc, about, animacion, login, register, exit

urlpatterns = [
    path('', home, name = 'home'),
    path('calc/', calc, name  = 'calc'),
    path('about/', about, name='about'),
    path('animacion/', animacion, name = 'animacion'),
    path('login/', login, name = 'login'),
    path('logout/', exit, name='exit'),
    path('register/', register, name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    

]