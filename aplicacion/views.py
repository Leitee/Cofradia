from django.shortcuts import render
from django.http import HttpResponse
from models import Usuario

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

def nuevoUSuario(request):
	nuevoUser = Usuario(nombre=request.GET['nombre'],
		apellido=request.GET['apellido'],user=request.GET['user'],pas=request.GET['pas'])
	nuevoUser.save()

def mostrarPubli(request):
	return render(request,'mostrarPubli.html')