from django.urls import path
from.views import solicitud, listar_solicitudes, modificar_solicitudes, eliminar_solicitudes

urlpatterns = [
    path('solicitud/', solicitud, name="solicitudes"),
    path('listar-solicitudes/', listar_solicitudes, name="listar_solicitudes"),
    path('modificar-solicitudes/<id>/', modificar_solicitudes, name="modificar_solicitudes" ),
    path('eliminar-solicitudes/<id>/', eliminar_solicitudes, name="eliminar_solicitudes"),
]