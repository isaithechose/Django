# Generated by Django 4.2.14 on 2024-07-20 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Numeros',
            new_name='Prueba',
        ),
        migrations.RenameField(
            model_name='prueba',
            old_name='subtitulo',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='prueba',
            old_name='titulo',
            new_name='title',
        ),
    ]
