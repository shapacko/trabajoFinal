from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bibliotecas.forms import PrestamoForm
from bibliotecas.models import Socio, Libro


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
                return HttpResponse("No hay copias!")
            for copia in libro.copia_set.all():
                if copia.estado == 'disponible':
                    copia.estado = 'prestado'
                    copia.save()
                    return HttpResponse("Gracias!")
            # return HttpResponseRedirect('/thanks/')
            return HttpResponse("No hay copias disponibles!")
    else:
        form = PrestamoForm()

    return render(request, 'bibliotecas/prestamos.html', {'form': form})

# def prestamo(request, socio_id, isbn):
def prestamo(request):
    return HttpResponse("Gracias!")

def devolucion(request, socio_id, nro_inventario):
    return HttpResponse("Devolución")

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

def libro(request, isbn):
    return HttpResponse("Info del libro " + isbn)

def morosos(request):
    return HttpResponse("Morosos")

def prestamo_fecha(request, fecha):
    return HttpResponse("Lista de prestamos")

def moroso_fecha(request, fecha):
    return HttpResponse("Lista de morosos")