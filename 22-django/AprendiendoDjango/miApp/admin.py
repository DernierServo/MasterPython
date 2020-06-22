from django.contrib import admin
from .models import Article, Category

# Register your models here.
# Ds: Para generar un CRUD de cada modelo en el /admin de Django.
admin.site.register(Article)
admin.site.register(Category)