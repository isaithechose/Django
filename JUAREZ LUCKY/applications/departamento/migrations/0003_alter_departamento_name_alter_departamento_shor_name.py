# Generated by Django 4.2.14 on 2024-07-22 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_anulate_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=15, unique=True, verbose_name='Nombres '),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(max_length=5, verbose_name='Numero'),
        ),
    ]
