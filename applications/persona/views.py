from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView
)
from applications.empleado.models import Empleado

class ListaAllEmpleados(ListView):
    template_name='persona/list_all.html'
    model=Empleado

class ListaByAreaEmpleados(ListView):
    """ lista empleados de un area """
    template_name='persona/list_all.html'
    model=Empleado