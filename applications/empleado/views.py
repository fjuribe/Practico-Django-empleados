from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class EmpleadoView(TemplateView):
    template_name="empleado/empleado.html"
