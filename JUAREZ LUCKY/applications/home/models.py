from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=15)
    numero_celular = models.CharField(max_length=10)
    numero = models.IntegerField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} {self.apellidos} - {self.numero} ({self.numero_celular})'
