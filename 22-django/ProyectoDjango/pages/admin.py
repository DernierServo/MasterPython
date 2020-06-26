from django.contrib import admin
from .models import Page

# ds: Configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  #ds: agrega campos de lectura
    search_fields = ('title', 'content')    #ds: Agrega buscador
    list_filter = ('visible',)  #Filtro para búsqueda
    list_display = ('title', 'visible', 'created_at')   #Mostrar en columnas de vista previa
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

# ds: Configuración del Panel
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle