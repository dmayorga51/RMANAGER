from django.contrib import admin
from .models import Tipo, Estado, Prioridad, Criticidad, Solicitud, Imputacion
# Register your models here.


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "usuario_solicitante", "tipo", "estado", "prioridad", "criticidad", "fecha_ingreso"]
    ## list_editable = ["usuario_solicitante", "tipo", "estado", "prioridad", "criticidad"]
    search_fields = ["nombre", "descripcion", "usuario_solicitante", "tipo", "estado", "prioridad", "criticidad"]
    list_filter = ["usuario_solicitante", "tipo"]
    list_per_page = 5

admin.site.register(Tipo) ## esto es para que el modelo se visualice en el admin
admin.site.register(Estado)
admin.site.register(Prioridad)
admin.site.register(Criticidad)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Imputacion)