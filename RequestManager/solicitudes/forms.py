from django import forms
from .models import Solicitud ## importar el modelo

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        ##fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"] ## esto es pra listar de forma individual
        fields = '__all__' ## con este se listan todos los campos del modelo