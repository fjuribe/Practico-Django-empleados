from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

#import models
from .models import Prueba

class PruebaView(TemplateView):
    template_name='home/prueba.html'

class PruebaListView(ListView):    
    queryset=['1','4','5','10']
    context_object_name='listanumeros'
    template_name="home/lista.html"


class ListarPruebaView(ListView):   
    model=Prueba
    context_object_name='lista'
    template_name="home/lista_prueba.html"


class PruebaCreateView(CreateView):    
    model=Prueba
    fields=['titulo','subtitulo','cantidad']
    template_name="home/add_prueba.html"

    
    



