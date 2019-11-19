from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import ServicePost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import *
# Create your views here.

def post_principal(request):
    return render(request, 'dogs/principal.html', {})

def post_formulario(request):
    return render(request, 'dogs/formulario.html', {})

def post_servicios(request):
    return render(request, 'dogs/servicios.html', {})

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)    


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "dogs/inicio.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

    
def crear_usuario(request):
    if request.method == 'ServicePost':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #  log the user in
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()        
  
    return render(request, 'dogs/registro.html', { 'form': form })  
   
def dogs_list(request):
    dogs = ServicePost.objects.order_by('codigo')     
    return render(request, 'dogs/formulario.html', { 'dogs': dogs } )      
  