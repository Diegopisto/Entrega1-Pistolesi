from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from Club_app.models import Actividades, Profesores

# Create your views here.

def inicio(self):
    return render(self, "inicio.html")

def profesores(request):

    if request.method == "POST":

        profesores = Profesores(nombre=request.POST["nombre"], actividad=request.POST["actividad"], turno=request.POST["turno"])
        
        profesores.save()

        return render(request,"cargaexitosa.html")

    return render(request,"profesores.html")



def actividades(request):
    
    if request.method == "POST":

        actividades = Actividades(actividad=request.POST["actividad"], turno=request.POST["turno"])
        
        actividades.save()

        return render(request,"cargaexitosa.html")

    return render(request,"actividades.html")
    




def alumnos(request):
    return render(request,"alumnos.html")

### BUSQUEDA de profesores que dictan clases de: / LA BUSQUEDA EN LA COLUMANA ACTIVIDAD

def busquedaprofesor(request):

    return render(request,"busquedaprofesor.html")

# BUSCANDOPROFE SE RENDERIZA EN RBUSQUEDAPROFESOR
def buscandoprofe(request):

    if request.GET["actividad"]:

        actividad = request.GET["actividad"]

        profesores = Profesores.objects.filter(actividad__icontains=actividad)

        return render(request, "rbusquedaprofesor.html", {"profesores":profesores, "actividad":actividad})

    else:
        mensaje = "No se ingreso parametros de busqueda"
    return HttpResponse(mensaje)
