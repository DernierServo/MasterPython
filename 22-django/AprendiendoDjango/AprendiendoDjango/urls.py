"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Importar app con mis vistas
#from miApp import views
import miApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miApp.views.index, name="n_index"),
    path('inicio/', miApp.views.index, name="n_inicio"),
    path('hola-mundo/', miApp.views.hola_mundo, name="n_hola_mundo"),
    path('otra-pagina/', miApp.views.otra_pagina, name="n_otra_pagina"),
    path('otra-pagina/<int:redirigir>', miApp.views.otra_pagina, name="n_otra_pagina"),    
    path('contacto/', miApp.views.contacto, name="n_contacto"),
    path('contacto/<str:nombre>/', miApp.views.contacto, name="n_contacto"),
    path('contacto/<str:nombre>/<str:apellido>/', miApp.views.contacto, name="n_contacto"),
    path('contacto/<str:nombre>/<str:apellido>/<int:edad>/', miApp.views.contacto, name="n_contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>/', miApp.views.crear_articulo, name='n_crear_articulo'),
    path('mostrar-articulo/<int:p_id>/', miApp.views.mostrar_articulo, name='n_mostrar_articulo'),
    path('editar-articulo/<int:p_id>/', miApp.views.editar_articulo, name='n_editar_articulo'),
]
