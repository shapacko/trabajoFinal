from django.conf.urls import url
from . import views

##ToDo:validar largo de series y fechas
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^prestamo/$', views.prestamo, name='prestamo'),
    url(r'^devoluciones/$', views.devoluciones, name='devoluciones'),


    url(r'^socios/$', views.socios, name='socios'),
    url(r'^socio/(?P<socio_id>[0-9]+)/$', views.socio, name='socio'),

    url(r'^libros/$', views.libros, name='libros'),
    url(r'^libro/(?P<isbn>[0-9]+)/$', views.libro, name='libro'),

    url(r'^copias/$', views.copias, name='copias'),
    url(r'^copia/(?P<nro_inventario>[0-9]+)/$', views.copia, name='copia'),

    url(r'^morosos/$', views.morosos, name='morosos'),
    url(r'^prestamo_fecha/$', views.prestamo_fecha, name='prestamo_fecha'),
    url(r'^morosos_fecha/(?P<fecha>[0-9]+)/$', views.moroso_fecha, name='moroso_fecha'),
]
