from django.shortcuts import render
from django.http import HttpResponse
from models import Usuario, Publicacion, Categoria
import datetime

def iniciarSesion(request):
	return render(request,'iniciarSesion.html')

def buscarUsuario(request):
	if Usuario.objects.filter(user=request.GET['user']).exists():
		if Usuario.objects.filter(user=request.GET['user']).filter(pas=request.GET['password']).exists():
			return HttpResponse('Bienvenido a Cofradia')
		else:
			return HttpResponse('Password Incorrecto')
	else:
		return HttpResponse('Nombre de Usuario Incorrecto')

def crearUsuario(request):
	return render(request,'crearUsuario.html')

def nuevoUsuario(request):
	nuevoUser = Usuario(nombre=request.GET['nombre'],apellido=request.GET['apellido'],user=request.GET['user'],pas=request.GET['pass1'],fNacimiento = request.GET['fechaNacimiento'],sexo= request.GET['sex'],email= request.GET['eMail'],telefono= request.GET['unTel'])
	nuevoUser.save()
	return HttpResponse('Usuario creado exitosamente')

#def nuevaPubli(request):
	#nuevaPubli = Publicacion(nombre=request.GET['nombre'],fechaInicio=datetime.datetime.now(),Categoria(nombre= request.GET['nombreUsu'], descripcion= request.GET['descripCat'], descripcion= request.GET['descripcion']))

def mostrarPubli(request):
	return render(request,'mostrarPubli.html')