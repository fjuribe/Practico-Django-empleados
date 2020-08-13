from django.urls import path
from .import views

urlpatterns = [
    path('empleado/',views.EmpleadoView.as_view()),
]
