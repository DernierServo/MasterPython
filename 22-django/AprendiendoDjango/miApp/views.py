# render: Devuelve la template que queremos cargar desde la View, pero debe buscarla
#         dentro de mi App (para lo cual debo agregarla en el 'settings.py' en INSTALLED_APPS)

# request: Es un parámetro que permite recibir datos de peticiones a la URL donde se use. 
#          Se debe de pasar a todos los métodos de la vista.

# HttpResponse: Respuesta Http

# redirect: Redirecciona a otras rutas (URL's)

# MTV -> M: Model (BD), T: Vista (HTML, templates), V: Acciones (métodos)
###########################################################################################

from django.shortcuts import render, HttpResponse, redirect
from miApp.models import Article
from django.db.models import Q

layout = ""


def index(request):
    anho_ini = 2021
    rango_anhos = range(anho_ini, 2051)

    nombre = 'Dernier Servo'
    lenguajes = ['Python', 'C', 'C++', 'Julia', 'Go', 'Javascript']
    #lenguajes = []

    return render(
        request, 
        'index.html',
        {
            'title': 'Inicio',
            'nombre': nombre,
            'lps': lenguajes,
            'mi_variable': 'Soy un dato que está en la vista principal!',
            'anhos': rango_anhos
        }
    )


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def otra_pagina(request, redirigir=0):
    if redirigir == 1:
        #return redirect("/")
        #return redirect('/contacto/dernier/servo/19')
        return redirect('n_contacto', nombre='Pedro', apellido='Picapiedra', edad=45)
    return render(
        request, 
        'otra_pagina.html',
        {
            'texto_pruebarueba': '',
            'lista_prueba': ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
        }
    )


def contacto(request, nombre="", apellido="", edad=None):
    """ Estos parámetros deben tener el mismo nombre y tipo que el que se especifica
        en el urls.py
    """
    html = ""
    
    if nombre and apellido and edad:
        html += '<p>El nombre completo es:</p>'
        html += f'<h3>{nombre} {apellido}</h3>'
    response = HttpResponse(layout + f"<h2>Contacto: </h2>" + html)
        
    return response


def crear_articulo(request, title='', content='', public=''):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

     # método save() es para guardarlo en la BD.
    articulo.save()

    return HttpResponse(f'<p>Artículo creado: </p><p><strong>Título: </strong>{articulo.title}</p> <p><strong>Contenido: </strong>{articulo.content }</p>')


def mostrar_articulo(request, p_id):
    try:
        #articulo = Article.objects.get(id='7', public=True)
        articulo = Article.objects.get(id=p_id)
        response = f'Articulo: </br> {articulo.id} - {articulo.title}'
    except:
        response = '<h1>Artículo no encontrado</h1>'
    return HttpResponse(response)


def editar_articulo(request, p_id):

    articulo = Article.objects.get(id=p_id)

    articulo.title = 'Chapulín Colorado'
    articulo.content = 'Más noble que una lechuga, Más fuerte que un ratón.'

    articulo.save()

    return HttpResponse(f'<p>Artículo Editado: </p><p><strong>Título: </strong>{articulo.title}</p> <p><strong>Contenido: </strong>{articulo.content }</p>')


def listar_articulos(request):
    
    #ORM Django:
    #articulos = Article.objects.all()
    #articulos = Article.objects.filter(id__gt=3).exclude(public=False) #Excluye
    #articulos = Article.objects.filter(public=True) #Filtra por Atributo
    #articulos = Article.objects.filter(public=True, id=3) #AND, varias condiciones
    #articulos = Article.objects.filter(title__contains='pelo') #"like"
    #articulos = Article.objects.filter(id__gt=3) #'>'
    #articulos = Article.objects.filter(id__gte=3) #'>='
    #articulos = Article.objects.filter(id__lt=3) #'>'
    #articulos = Article.objects.filter(id__lte=3) #'>='    
    #articulos = Article.objects.all()  #Trae TODOS los elemntos
    #articulos = Article.objects.order_by('id')[1:3] #Filtro por cantidad de elementos
    #articulos = Article.objects.all()
    #articulos = Article.objects.order_by('title') #Ordenar por Título Creciente
    #articulos = Article.objects.order_by('-title') #Ordenar por Título decreciente
    #OR
    articulos = Article.objects.filter(
        Q(title__contains='pelo') | Q(title__contains='moha')
    )

    
    #SQL Puro:
    #articulos = Article.objects.raw(
    #    """
    #    SELECT * 
    #    FROM miApp_article
    #    WHERE id>3 AND id<=7 AND public=True
    #    """
    #)



    return render(
        request, 
        'articulos.html', 
        {
            'articulos': articulos
        }
    )


def borrar_articulo(request, p_id):
    try:
        articulo = Article.objects.get(id=p_id)
        articulo.public = 0
        articulo.save()
        return redirect('n_articulos')
    except:
        return HttpResponse('<h1>Artículo no encontrado</h1>')
