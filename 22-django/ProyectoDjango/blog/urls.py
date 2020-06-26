from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name='n_articulos'),
    path('categoria/<int:p_category_id>/', views.category, name='n_category'),
    path('articulo/<int:p_article_id>/', views.article, name='article')
]
