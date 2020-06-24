from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

# ds: Configuración del Panel
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle