from django.conf.urls import url
from . import views

##ToDo:validar largo de series y fechas
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prestamos/$', views.prestamos, name='prestamos'),
    # url(r'^prestamo/(?P<socio_id>[0-9]+)/(?P<isbn>[0-9]+)/$', views.prestamo, name='prestamo'),
    url(r'^devolucion/(?P<socio_id>[0-9]+)/(?P<nro_inventario>[0-9]+)/$', views.devolucion, name='devolucion'),

    url(r'^socios/$', views.socios, name='socios'),
    url(r'^socio/(?P<socio_id>[0-9]+)/$', views.socio, name='socio'),
    url(r'^copia/(?P<nro_inventario>[0-9]+)/$', views.copia, name='copia'),
    url(r'^libro/(?P<isbn>[0-9]+)/$', views.libro, name='libro'),
    url(r'^morosos/$', views.morosos, name='morosos'),
    url(r'^prestamo_fecha/(?P<fecha>[0-9]+)/$', views.prestamo_fecha, name='prestamo_fecha'),
    url(r'^moroso_fecha/(?P<fecha>[0-9]+)/$', views.moroso_fecha, name='moroso_fecha'),
]