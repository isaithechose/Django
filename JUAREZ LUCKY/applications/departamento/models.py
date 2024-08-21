from django.db import models


# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombres ', max_length=15, unique=True)
    shor_name = models.CharField('Numero', max_length=5)
    anulate = models.BooleanField('Pagado', default=False)

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name + '-'
