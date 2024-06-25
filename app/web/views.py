from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
# Create your views here.

def home(request):
    return render(request, 'web/home.html')

@login_required
def animacion(request):
    return render(request, 'web/animacion.html')

def calc(request):
    return render(request,'web/calc.html')

def about(request):
    return render(request, 'web/about.html')

def login (request):
    return render (request, 'registration/login.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        "form": CustomUserCreationForm()
        
    }
    
    if request.method  == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            auth_login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html', data)


