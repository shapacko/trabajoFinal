Aclaraciones sobre el entregable:

1. El nombre de la app no es biblio sino bibliotecas. Más allá que en las urls luego se use biblio.
2. Me tomé la libertad de modificar algunas vistas que pedía la letra:

  Dado que utilicé formularios para ingresar los datos donde se requerían las siguientes vistas cambiaron:
    a. biblio/prestamo/{id_socio}/{ISBN} se sustituyó por biblio/prestamo/$.
    b. biblio/devolucion/{id_socio}/{nro_inventario} se sustituyó por biblio/devoluciones/$.

  Para las vistas de consulta de info (socios, libros y copias) se agregó una vista previa a la que pedía la letra en la cual se listan los datos existentes y al seleccionar uno ahí si se llama a la vista que pide la letra.

  Para las vistas 8 y 9 tambien se utilizaron formularios, por lo que las mismas no reciben un parametro fecha sino que se ingresa la fecha en pantalla y se muestran los resultados en la misma pantalla.
