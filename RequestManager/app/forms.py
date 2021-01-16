from django import forms
from .models import Contacto ## importar el modelo

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        ##fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"] ## esto es pra listar de forma individual
        fields = '__all__' ## con este se listan todos los campos del modelo