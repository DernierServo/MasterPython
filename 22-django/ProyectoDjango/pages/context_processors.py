from pages.models import Page

def get_pages(request):

    # Similar a: SELECT id, title, slug FROM Page
    pages = Page.objects.values_list('id', 'title', 'slug')
    #pages = Page.objects.all() #Retorna lista de Objetos
    #pages = Page.objects.values_list('title', flat=True) #Retorna lista de cadenas

    return {
        'pages': pages
    }