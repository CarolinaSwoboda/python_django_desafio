# Generated by Django 4.0.5 on 2022-06-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiPrimerMVTApp', '0003_familiar_delete_parentesco_delete_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('relacion', models.PositiveSmallIntegerField(choices=[(1, 'Papá/Mamá'), (2, 'Hermano/Hermana'), (3, 'Tío/Tía'), (4, 'Abuelo/Abuela'), (5, 'Primo/Prima')], verbose_name='Relación')),
                ('edad', models.IntegerField(verbose_name='Edad')),
            ],
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
    ]
