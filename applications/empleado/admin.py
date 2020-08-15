from django.contrib import admin

# Register your models here.
from .models import Empleado,Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'fieldName',
        'last_name',
        'departamento',
        'job',
    )
    search_fields=('fieldName',)
admin.site.register(Empleado,EmpleadoAdmin)