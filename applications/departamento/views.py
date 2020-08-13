from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class DepartamentoView(TemplateView):
    template_name='departamento/depa.html'
