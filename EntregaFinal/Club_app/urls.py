from django.urls import path

from Club_app.views import actividades, alumnos, buscando_profe, inicio, profesores, busqueda_profesor, listado_actividades

urlpatterns = [
    path("", inicio),
    path("Club_app/profesores/", profesores, name="profesores"),
    path("Club_app/busquedaprofesor/", busqueda_profesor, name="busquedaprofesor"),
    path("Club_app/buscandoprofe/", buscando_profe, name="buscandoprofe"),
    path("Club_app/actividades/", actividades, name="actividades"),
    path("Club_app/alumnos/", alumnos, name="alumnos"),
    path("Club_app/listaactividades/", listado_actividades, name="listaactividades"),
]