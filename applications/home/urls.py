from django.urls import path

from .import views

urlpatterns = [
    path('',views.PruebaView.as_view()),
    path('home/', views.PruebaView.as_view()),
    path('lista/',views.PruebaListView.as_view()),
    path('lista_prueba/',views.ListarPruebaView.as_view()),
    path('add/',views.PruebaCreateView.as_view()),
    
]