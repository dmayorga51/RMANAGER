# Generated by Django 3.1.3 on 2020-11-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='archivo',
            field=models.FileField(null=True, upload_to='productos'),
        ),
    ]
