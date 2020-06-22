from django.contrib import admin
from .models import Article, Category

# Register your models here.
#"ModelAdmin" es la clase que permite modificar el panel de Administración
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Ds: Para generar un CRUD de cada modelo en el /admin de Django.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)