from django.urls import path

from Club_app.views import actividades, alumnos, buscandoprofe, busquedaprofesor, inicio, listadoactividades, profesores 

urlpatterns = [
    path("", inicio),
    path("profesores/", profesores, name="profesores"),
    path("busquedaprofesor/", busquedaprofesor, name="busquedaprofesor"),
    path("buscandoprofe/", buscandoprofe, name="buscandoprofe"),
    path("actividades/", actividades, name="actividades"),
    path("alumnos/", alumnos, name="alumnos"),
    path("listaactividades/", listadoactividades, name="listaactividades"),
]