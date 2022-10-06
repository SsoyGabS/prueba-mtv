from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from mtv.models import familia
def view(request):
    return HttpResponse("si pude!")
def el_template(request, nombre):
    template = loader.get_template('tamplate.html')
    template_renderizado = template.render('este es mi template')
    return HttpResponse(template_renderizado)
def crear_familiar(request):
    familiar1= familia(nombre='Alberto', apellido='Perez', parentezco='Sobrino', edad= 15)
    familiar2= familia(nombre='Miguel', apellido='Migliore', parentezco='Hermano', edad=30)
    familiar3= familia(nombre='Josefina', apellido='Olmedo', parentezco='Prima', edad=27)
    familiar1.save()
    familiar2.save()
    familiar3.save()
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render()
    return HttpResponse(template_renderizado)
def ver_familia(request):
    familiar = familia.objects.all()
    template = loader.get_template('ver_familia.html')
    template_renderizado = template.render(familiar)
    return HttpResponse(template_renderizado)