# Generated by Django 3.1.3 on 2020-11-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_producto_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_fabricacion',
            field=models.DateField(null=True),
        ),
    ]
