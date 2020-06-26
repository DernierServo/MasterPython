from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)  #ds: agrega campos de lectura
    search_fields = ('name', 'description')    #ds: Agrega buscador
    list_display = ('name', 'description', 'created_at')   #Mostrar en columnas de vista previa
    ordering = ('-created_at',)    


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')  #ds: agrega campos de lectura
    search_fields = ('title', 'content', 'user__username', 'categories__name')    #ds: Agrega buscador
    list_filter = ('public', 'user__username', 'categories__name')  #Filtro para búsqueda
    list_display = ('title', 'user', 'image', 'public', 'created_at')   #Mostrar en columnas de vista previa
    ordering = ('-created_at',)    

    # Para guardar el usuario de la sesión en el campo usuario del modelo Article
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)