# Generated by Django 3.1.3 on 2020-11-14 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_producto_fecha_ingreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_ingreso',
        ),
    ]
