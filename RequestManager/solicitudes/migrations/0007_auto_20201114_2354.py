# Generated by Django 3.1.3 on 2020-11-15 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0006_auto_20201114_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='criticidad',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.criticidad'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='prioridad',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.prioridad'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='usuario_solicitante',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
