from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template
def view(request):
    return HttpResponse("si pude!")
def mi_template(request):
    cargar_archivo = open(r'C:\Users\GabS\Desktop\vs code\proyecto\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close 
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado) 