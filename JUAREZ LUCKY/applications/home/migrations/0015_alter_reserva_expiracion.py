# Generated by Django 4.2.14 on 2024-08-05 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_reserva_expiracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 2, 29, 37, 194729, tzinfo=datetime.timezone.utc)),
        ),
    ]
