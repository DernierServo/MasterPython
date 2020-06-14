# request: Es un parámetro que permite recibir datos de peticiones a la URL donde se use. 
#          Se debe de pasar a todos los métodos de la vista.

# HttpResponse: Respuesta Http

# redirect: Redirecciona a otras rutas (URL's)

# MTV -> M: Model (BD), T: Vista (HTML, templates), V: Acciones (métodos)
###########################################################################################

from django.shortcuts import render, HttpResponse, redirect

layout = """
    <h1>Sitio web con Django | Dernier Servo</h1>
    <hr/>
    <ul>
        <li>
            <a href = '/'>Inicio</a>
        </li>
        <li>
            <a href = '/hola-mundo'>Hola mundo</a>
        </li> 
        <li>
            <a href = '/otra-pagina'>Otra página</a>
        </li>      
        <li>
            <a href = '/contacto2'>Contacto</a>
        </li>       
    </ul>
    <hr/>
"""

def index(request):
    return HttpResponse(layout + """
        <h1>Inicio</h1>
        <h2>Esta es la página principal</h2>
        <h3>Desarrollado por: DServo-Labs &copy; 2020</h3>
    """)

def hola_mundo(request):
    return HttpResponse(layout + """
        <h1>Hola mundo con Django!!</h1>
        <h2>Desarrollado por DServo-Labs &copy; 2020</h2>
    """)

def otra_pagina(request, redirigir=0):
    if redirigir == 1:
        #return redirect("/")
        #return redirect('/contacto/dernier/servo/19')
        return redirect('n_contacto', nombre='Pedro', apellido='Picapiedra', edad=45)
    return HttpResponse(layout + """
        <h1>Otra página!</h1>
        <h2>Esta es una página alternativa de la principal.</h2>
    """)
    return response

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