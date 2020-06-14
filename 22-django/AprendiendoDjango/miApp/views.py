# render: Devuelve la template que queremos cargar desde la View, pero debe buscarla
#         dentro de mi App (para lo cual debo agregarla en el 'settings.py' en INSTALLED_APPS)

# request: Es un parámetro que permite recibir datos de peticiones a la URL donde se use. 
#          Se debe de pasar a todos los métodos de la vista.

# HttpResponse: Respuesta Http

# redirect: Redirecciona a otras rutas (URL's)

# MTV -> M: Model (BD), T: Vista (HTML, templates), V: Acciones (métodos)
###########################################################################################

from django.shortcuts import render, HttpResponse, redirect

layout = ""

def index(request):
    return render(request, 'index.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def otra_pagina(request, redirigir=0):
    if redirigir == 1:
        #return redirect("/")
        #return redirect('/contacto/dernier/servo/19')
        return redirect('n_contacto', nombre='Pedro', apellido='Picapiedra', edad=45)
    return render(request, 'otra_pagina.html')

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