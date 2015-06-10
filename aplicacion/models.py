from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	user = models.CharField(max_length=20)
	pas = models.CharField(max_length=15)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length = 30)

class SubCategoria(models.Model):
	nombre = models.CharField(max_length = 30)
	categoria = models.ForeignKey(Categoria)	

class Objeto(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 255)
	subcategoria = models.ForeignKey(SubCategoria)
	usuario = models.ForeignKey(Usuario)

