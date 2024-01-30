from django.http import HttpResponse
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

def probando_template(request):
    #Abrimos plantilla
    mi_html = open('C:\\Users\\jp_lu\\OneDrive\\Escritorio\\CoderHouse\\Clase_17\\Plantillas\\template1.html') 
    #Creamos planitlla con la clase Template
    plantilla = Template(mi_html.read())
    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()
    #Creamos un contexto
    contexto = Context()
    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Hola Django - Coder")  

def segunda_vista(request):
    return HttpResponse("<br><br>Esta es mi segunda vista")