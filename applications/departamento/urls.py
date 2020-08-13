from django.urls import path
from .import views
    
urlpatterns = [
    path('departamento/',views.DepartamentoView.as_view()),

]
