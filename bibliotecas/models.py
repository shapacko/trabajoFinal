from django.db import models

class Libro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_ingreso =models.DateField()

    def __str__(self):
        return self.titulo + " - " + self.autor

class Copia(models.Model):
    nro_inventario = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return "Copia " + str(self.nro_inventario) + " de " + str(self.libro)

class Socio(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.id + " - " + self.nombre

class Prestamo(models.Model):
    copia = models.ForeignKey(Copia)
    socio = models.ForeignKey(Socio)
    fecha_comienzo = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20)

    def __str__(self):
        return "Préstamo de " + str(self.copia) + " a " + str(self.socio)
