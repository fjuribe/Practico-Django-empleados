from django.db import models
from applications.departamento.models import Departamento

# Create your models here.
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
    #fieldName = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

    
    
    
    

