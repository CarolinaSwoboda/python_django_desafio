# Generated by Django 4.0.5 on 2022-06-16 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiPrimerMVTApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='año_nacimiento',
            new_name='anio_nacimiento',
        ),
    ]
