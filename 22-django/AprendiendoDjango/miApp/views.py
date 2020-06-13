# request: Es un parámetro que permite recibir datos de peticiones a la URL donde se use. 
#          Se debe de pasar a todos los métodos de la vista.

# HttpResponse: Respuesta Http

# MTV -> M: Model (BD), T: Vista (HTML, templates), V: Acciones (métodos)
###########################################################################################

from django.shortcuts import render, HttpResponse

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

def otra_pagina(request):
    return HttpResponse(layout + """
        <h1>Otra página!</h1>
        <h2>Esta es una página alternativa de la principal.</h2>
    """)
    return response

