from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField(null=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    archivo = models.FileField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

opciones_consultas =[              ## este listados es para setear en duro las opciones de consulta de la clase Contacto
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas) ##choices opciones consulta es para que tome el listado opciones consultas
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre