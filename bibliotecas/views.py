import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from bibliotecas.forms import PrestamoForm, DevolucionForm, ListaPrestamosForm
from bibliotecas.models import Socio, Libro, Prestamo, Copia


def index(request):
    return render(request, 'bibliotecas/index.html')

def prestamo(request):
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
                    prestamo.fecha_comienzo = datetime.date.today()
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
            copia = Copia.objects.get(nro_inventario=form.cleaned_data['nro_inventario'])
            prestamo = Prestamo.objects.get(socio=form.cleaned_data['socio'], copia=form.cleaned_data['nro_inventario'])
            if prestamo:
                copia.estado = "disponible"
                copia.save()
                if datetime.date.today() > prestamo.fecha_fin:
                    socio.estado = "moroso"
                    socio.save()
                prestamo.estado="terminado"
                prestamo.save()
                return HttpResponse("Copia devuelta con exito.")
            else:
                raise Http404("Préstamo inexistente.")
    else:
        form = DevolucionForm()

    return render(request, 'bibliotecas/devoluciones.html', {'form': form})

def socios(request):
    lista_socios = Socio.objects.all()
    context = {'lista_socios': lista_socios}
    return render(request, "bibliotecas/socios.html", context)

def socio(request, socio_id):
    socio = Socio.objects.get(id=socio_id)
    context = {'socio': socio}
    return render(request, "bibliotecas/socio.html", context)

def copias(request):
    lista_copias = Copia.objects.all()
    context = {'lista_copias': lista_copias}
    return render(request, "bibliotecas/copias.html", context)

def copia(request, nro_inventario):
    copia = Copia.objects.get(nro_inventario=nro_inventario)
    context = {'copia': copia}
    prestamo = Prestamo.objects.filter(copia=copia.nro_inventario, estado="pendiente")
    if prestamo:
        context.update({'prestamo': prestamo})
    return render(request, "bibliotecas/copia.html", context)

def libros(request):
    lista_libros = Libro.objects.all()
    context = {'lista_libros' : lista_libros}
    return render(request, "bibliotecas/libros.html", context)

def libro(request, isbn):
    libro = Libro.objects.get(isbn=isbn)
    context = {'libro': libro}
    return render(request, "bibliotecas/libro.html", context)

def morosos(request):
    lista_morosos = Socio.objects.filter(estado="moroso")
    context = {'lista_morosos' : lista_morosos}
    return render(request, "bibliotecas/morosos.html", context)

def prestamo_fecha(request):
    if request.method == 'POST':
        form = ListaPrestamosForm(request.POST)
        if form.is_valid():
            lista_prestamos = Prestamo.objects.filter(fecha_comienzo=form.cleaned_data['fecha'])
            context = {'form': form, 'lista_prestamos': lista_prestamos}
    else:
        form = ListaPrestamosForm()
        context = {'form': form}

    return render(request, 'bibliotecas/lista_prestamos.html', context)

def moroso_fecha(request, fecha):
    return HttpResponse("Lista de futuros morosos")
