from django.contrib import admin

from MiPrimerMVTApp.models import *

# Register your models here.

class FamiliareAdmin(admin.ModelAdmin):
    
    list_display = ("nombre","apellido","relacion","edad")
    
admin.site.register(Familiare, FamiliareAdmin)

# administrador
# usuario: admin
# contraseña: admin