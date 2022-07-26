from django.contrib import admin

############IMPORTO LOS MODELOS  ####

from Club_app.models import Profesores, Alumnos, Actividades

class Alumnosadmin(admin.ModelAdmin):
    list_display = ["nombre","edad","actividad","turno"]
    search_fields = ["nombre","edad","actividad","turno"]

class Profesoresadmin(admin.ModelAdmin):
    list_display = ["nombre","actividad","turno"]

class Actividadesadmin(admin.ModelAdmin):
    list_display = ["actividad","turno"]


# Register your models here.
admin.site.register(Profesores, Profesoresadmin)
admin.site.register(Alumnos, Alumnosadmin)
admin.site.register(Actividades, Actividadesadmin)

#USUARIO pisto
#clave 123456