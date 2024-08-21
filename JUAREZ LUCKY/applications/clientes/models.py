from django.db import models
from applications.departamento.models import Departamento
# Create your models here. relacion de base de datos
class Persona(models.Model):
    """ MOdelo para tabla"""
    JOB_CHOICES = (
        ('0', 'OPCION 1'),
        ('1', '2'),
        ('3', '3'),

    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    job = models.CharField('trabajo', max_length=15, choices=JOB_CHOICES)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name