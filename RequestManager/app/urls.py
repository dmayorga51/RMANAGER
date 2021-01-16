from django.urls import path
from.views import home, contacto, galeria
from solicitudes.views import solicitud, listar_solicitudes

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('solicitud/', solicitud, name="solicitudes"),
    path('listar-solicitudes/', listar_solicitudes, name="listar_solicitudes"),
    
]

