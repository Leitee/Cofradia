from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length= 50)
	descripcion = models.CharField(max_length= 200)

class Usuario(models.Model):
	nombre = models.CharField(max_length=50, null = False)
	apellido = models.CharField(max_length=50, null = True)
	user = models.CharField(max_length=20, unique = True)
	pas = models.CharField(max_length=15, null = False)
	fNacimiento = models.DateField()
	sexo = models.BooleanField()
	email = models.EmailField(max_length = 75)
	telefono = models.CharField(max_length = 20)

class Publicacion(models.Model):
	nombre = models.CharField(max_length=100)
	fechaInicio = models.DateField()
	fechaCierre = models.DateField()
	usuario = models.ForeignKey(Usuario)
	categoria = models.ForeignKey(Categoria)
	descripcion = models.CharField(max_length = 300)	


class Postulante(models.Model):
	usuario = models.ForeignKey(Usuario)
	publicacion = models.ForeignKey(Publicacion)

class Calificacion(models.Model):
	calificacion = models.IntegerField()
	tipo = models.BooleanField()
	usuario = models.ForeignKey(Usuario)
	publicacion = models.ForeignKey(Publicacion)