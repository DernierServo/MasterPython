from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='n_index'),
    path('inicio/', views.index, name='n_inicio'),
]