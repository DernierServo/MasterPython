from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(
        request, 
        'mainapp/index.html', 
        {
            'title': 'Inicio'
        }
    )

def about(request):
    return render(
        request, 
        'mainapp/about.html',
        {
            'title': 'Sobre nosotros'
        }
    )


def register_page(request):

    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado con éxito!')

            return redirect('n_inicio')

    return render(
        request, 
        'users/register.html',
        {
            'title': 'Registro',
            'register_form': register_form
        }

    )


def login_page(request):

    # Valida que la información esté llegando desde el Formulario: Método POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('n_inicio')
        else:
            messages.warning(request, 'No te has podido identificarsh!')

    return render(
        request, 
        'users/login.html',
        {
            'title': 'Identifícate'
        }
    )