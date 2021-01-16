from django.contrib import admin
from .models import Marca, Producto, Contacto ##importar modelelos
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 5


#admin.site.register(Marca) ## esto es para que el modelo se visualice en el admin
#admin.site.register(Producto, ProductoAdmin)
#admin.site.register(Contacto)