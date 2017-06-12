import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bibliotecas.forms import PrestamoForm, DevolucionForm
from bibliotecas.models import Socio, Libro, Prestamo


def index(request):
    return render(request, 'bibliotecas/index.html')

def prestamos(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            socio = Socio.objects.get(id=form.cleaned_data['socio'])
            if socio.estado == 'moroso':
                return HttpResponse("Socio moroso!")
            libro = Libro.objects.get(isbn=form.cleaned_data['isbn'])
            if libro.copia_set.count() < 1:
                return HttpResponse("No hay copias de este libro!")
            for copia in libro.copia_set.all():
                if copia.estado == 'disponible':
                    copia.estado = 'prestado'
                    copia.save()
                    prestamo = Prestamo()
                    prestamo.socio = socio
                    prestamo.copia = copia
                    prestamo.fecha_comienzo = datetime.date()
                    prestamo.fecha_fin = prestamo.fecha_comienzo + datetime.timedelta(days=7)
                    prestamo.estado = "pendiente"
                    prestamo.save()
                    return HttpResponse("Préstamo otorgado, gracias!")

            return HttpResponse("No hay copias disponibles!")
    else:
        form = PrestamoForm()

    return render(request, 'bibliotecas/prestamos.html', {'form': form})

def devoluciones(request):
    if request.method == 'POST':
        form = DevolucionForm(request.POST)
        if form.is_valid():
            socio = Socio.objects.get(id=form.cleaned_data['socio'])

def socios(request):
    lista_socios = Socio.objects.all()
    context = {'lista_socios': lista_socios}
    return render(request, "bibliotecas/socios.html", context)

def socio(request, socio_id):
    socio = Socio.objects.get(id=socio_id)
    context = {'socio': socio}
    return render(request, "bibliotecas/socio.html", context)

def copia(request, nro_inventario):
    return HttpResponse("Info de la copia " + nro_inventario)

def libros(request):
    lista_libros = Libro.objects.all()
    context = {'lista_libros' : lista_libros}
    return render(request, "bibliotecas/libros.html", context)

def libro(request, isbn):
    libro = Libro.objects.get(isbn=isbn)
    context = {'libro': libro}
    return render(request, "bibliotecas/libro.html", context)

def morosos(request):
    return HttpResponse("Morosos")

def prestamo_fecha(request, fecha):
    return HttpResponse("Lista de prestamos")

def moroso_fecha(request, fecha):
    return HttpResponse("Lista de morosos")