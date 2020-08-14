from django.db import models
from applications.departamento.models import Departamento

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('habilidades',max_length = 50)
    class meta:
        verbose_name='Habilidad'
        varbose_name_plural='Habilidad de Empleados'
    
    def __str__(self):
        return str(self.id)+'-'+self.habilidad
    


class Empleado(models.Model):
    JOB_CHOICES=(
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )

    """ Modelo para la tabla empleado"""
    fieldName = models.CharField('nombre',max_length = 60)
    last_name = models.CharField('apellido',max_length = 60)
    job       = models.CharField('trabajo',max_length =50,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #habilidad=models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    #fieldName = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

    
    
    
    

