# Generated by Django 3.1.3 on 2020-11-14 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_solicitud_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='productos'),
        ),
    ]
