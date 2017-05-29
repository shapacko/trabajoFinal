from django.contrib import admin
from .models import Libro, Copia, Socio, Prestamo

admin.site.register(Libro)
admin.site.register(Copia)
admin.site.register(Socio)
admin.site.register(Prestamo)
