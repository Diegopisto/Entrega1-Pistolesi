from django.template import loader
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from Club_app.models import Actividades, Alumnos, Profesores

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
    
    if request.method == "POST":

        alumnos = Alumnos(nombre=request.POST["nombre"], edad=request.POST["edad"],actividad=request.POST["actividad"], turno=request.POST["turno"])
        
        alumnos.save()

        return render(request,"cargaexitosa.html")

    return render(request,"alumnos.html")



def listado_actividades(request):

    lista = Actividades.objects.all()

    dic = {"activ":lista}

    plantilla = loader.get_template("listadoactividades.html")

    documento = plantilla.render(dic)

    return HttpResponse(documento)


### BUSQUEDA de profesores que dictan clases de: / LA BUSQUEDA EN LA COLUMANA ACTIVIDAD

def busqueda_profesor(request):

    return render(request,"busquedaprofesor.html")

# BUSCANDOPROFE SE RENDERIZA EN RBUSQUEDAPROFESOR
def buscando_profe(request):

    if request.GET["actividad"]:

        actividad = request.GET["actividad"]

        profesores = Profesores.objects.filter(actividad__icontains=actividad)

        return render(request, "rbusquedaprofesor.html", {"profesores":profesores, "actividad":actividad})

    else:
        mensaje = "No se ingreso parametros de busqueda"
    return HttpResponse(mensaje)
