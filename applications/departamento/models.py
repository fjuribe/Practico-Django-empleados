from django.db import models

# Create your models here.
class Departamento(models.Model):
    name=models.CharField('Nombre',max_length=50)
    shor_name=models.CharField('nombre corto',max_length=20,unique=True)
    anulate=models.BooleanField('Anulado',default=False)
    # FIELDNAME=models.DateField(,auto_now=False,auto_now_add=False)

    class Meta:
        verbose_name='Mi departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['-name']
        unique_together=('name','shor_name')


    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.shor_name
