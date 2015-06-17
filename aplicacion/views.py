from django.shortcuts import render
from django.http import HttpResponse
from models import Usuario, Categoria, Publicacion

def index(request):
	return render(request,'index.html',{'result':'','logueado':False})

def iniciarSesion(request):
	return render(request,'iniciarSesion.html',{'userValido':False,'pasValido':False})

def buscarUsuario(request):
	if Usuario.objects.filter(user=request.POST['user']).exists():
		if Usuario.objects.filter(user=request.POST['user']).filter(pas=request.POST['password']).exists():
			result = Usuario.objects.filter(user=request.POST['user'])
			return render(request,'index.html',{'result': result,'logueado':True})
		else:
			return render(request,'iniciarSesion.html',{'userValido':False,'pasValido':True})
	else:
		return render(request,'iniciarSesion.html',{'userValido':True,'pasValido':False})

def crearUsuario(request):
	return render(request,'crearUsuario.html',{'userValido':False,'pas':False})

def nuevoUSuario(request):
	if Usuario.objects.filter(user=request.GET['user']).exists():
		return render(request,'crearUsuario.html',{'userValido':True,'pas':False})
	else:
		if (request.GET['pass1'] == request.GET['pass2']): 
			nuevoUser = Usuario(nombre=request.GET['nombre'],apellido=request.GET['apellido'],user=request.GET['user'],pas=request.GET['pass1'],fNacimiento = request.GET['fechaNacimiento'],sexo= request.GET['sex'],email= request.GET['eMail'],telefono= request.GET['unTel'])
			nuevoUser.save()
			return HttpResponse('Usuario creado exitosamente')
		else:
			return render(request, 'crearUsuario.html',{'userValido':False,'pas':True})

def mostrarPubli(request):
	return render(request,'mostrarPubli.html')

#def nuevaPubli(request):
	#nuevaPubli = Publicacion(nombre=request.GET['nombre'],fechaInicio=datetime.datetime.now(),Categoria(nombre= request.GET['nombreUsu'], descripcion= request.GET['descripCat'], descripcion= request.GET['descripcion']))

def mostrarPubli(request):
	result = Publicacion.objects.distinct()
	return render(request,'mostrarPubli.html',{"result":result})

def verPerfil(request):
	return HttpResponse('Pantalla de administracion de datos de usuario')