from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import *
from .decorators import *

def connected_user(u):
	p = Person.objects.get(user = u)
	return p

# Create your views here.
#@login_required (login_url = '/login/')
def index_view(request):
	#return render(request, 'home/index.html', locals()) 
    return redirect('/login/')

'''
Authentication Section: login, logout, register, add_person views  
'''
def login_view (request):
	if request.method == 'POST':
		form = login_form(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			usuario = authenticate(username = u, password = p)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/my_sample_list/') 
			else:
				msg = 'usuario o clave incorrectos'	
	form = login_form()
	return render(request, 'home/login.html', locals())

def logout_view (request):
	logout(request)
	return redirect('/login/')

def register_view (request):
	formulario = register_form()
	usu = ""
	cor = ""
	cla_1 = ""
	cla_2 =""
	if request.method=='POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usu   = formulario.cleaned_data['user_name']
			cor   = formulario.cleaned_data['email']
			cla_1 = formulario.cleaned_data['pass_1']
			cla_2 = formulario.cleaned_data['pass_2']
			u = User.objects.create_user(username = usu, email=cor, password=cla_1)
			u.save()
			return redirect ('/login/')
		else:
			msj = 'no se pudo crear el usuario'			
	else:		
		return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

@login_required (login_url = '/login/')
def person_add_view2 (request):
	form_1 = register_form()
	form_2 = person_form()
	if request.method=='POST':
		form_1 = register_form(request.POST)
		form_2 = perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario 	= form_1.cleaned_data['usuario']
			correo 		= form_1.cleaned_data['correo']
			password_1 	= form_1.cleaned_data['clave_1']
			password_2 	= form_1.cleaned_data['clave_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			
			y = form_2.save(commit=False)
			y.user= u
			y.save()
			msg = "gracias por registrarse..."
			return redirect('/login/')

	return render(request,'person_add.html', locals())

def profile_edit_view (request):
	person = connected_user(request.user)
	user = User.objects.get(id = request.user.id)
	if request.method == 'POST':
		form_user = user_form(request.POST, instance=user)
		form = person_form(request.POST, request.FILES, instance=person)
		if form_user.is_valid() and form.is_valid():
			u = form_user.save(commit=False)
			u.username = form_user.cleaned_data['email']
			u.save()
			p = form.save(commit=False)
			p.user = u 
			p.save()
	else:
		form_user = user_form(instance=user)
		form = person_form(instance=person)
	return render(request, 'home/person_edit.html', locals())


def person_add_view(request):
    
	if request.method == 'POST':
		form_user = user_form(request.POST)
		form = person_form(request.POST, request.FILES)
		if form_user.is_valid() and form.is_valid():
			u = form_user.save(commit=False)
			u.set_password(form.cleaned_data['document'])
			u.username = form_user.cleaned_data['email']
			u.save()
			p = form.save(commit=False)
			p.user = u 
			p.save()
			messages.success(request, 'Usuario Creado')
	else:
		form_user = user_form()
		form = person_form()
	return render(request, 'home/person_add.html', locals())


def person_list_view (request):
	
	if request.method == 'GET':
		form = search_form()
		persons = Person.objects.filter()
	if request.method == 'POST':
		form = search_form(request.POST)
		if form.is_valid():
			s = form.cleaned_data['search']
			persons = Person.objects.filter(Q(user__first_name__icontains=s)|Q(user__last_name__icontains=s)|Q(document__icontains=s))
			if persons:
				pass
			else:
				msg = "No se encontraron resultados por favor cambie su criterio de busqueda"
	person = connected_user(request.user)
	users = persons.count()
	instructors =  Person.objects.filter(rol = 'instructor').count()
	aprentices = users - instructors
	return render(request, 'home/person_list.html', locals())

def person_delete_view(request, id_person):
	person = Person.objects.get(id = id_person)
	person.delete()
	user = User.objects.get(id = person.user.id)
	user.delete()
	return redirect('/person_list/')

def person_edit_view (request, id_person):
	person = Person.objects.get(id = id_person)
	user = User.objects.get(id= person.user.id)
	if request.method == 'POST':
		form_user = user_form(request.POST, instance=user)
		form = person_form(request.POST, request.FILES, instance=person)
		if form_user.is_valid() and form.is_valid():
			u = form_user.save(commit=False)
			u.username = form_user.cleaned_data['email']
			u.save()
			p = form.save(commit=False)
			p.user = u 
			p.save()
			return redirect('/person_detail/{}'.format(p.id))
	else:
		form_user = user_form(instance=user)
		form = person_form(instance=person)
	return render(request, 'home/person_edit.html', locals())

def person_detail_view(request, id_person):
	object = Person.objects.get(id = id_person)
	return render(request, 'home/person_detail.html',locals()) 



'''
Samples Section: list, add, detail, edit and delete views
'''

@login_required (login_url = '/login/')
def my_sample_list_view (request):
	person = connected_user(request.user)
	samples = Sample.objects.filter(person = person)
	samples_count = samples.count
	users_count = Person.objects.count()
	print(person)
	return render (request, 'home/sample_list.html', locals()) 

@login_required (login_url = '/login/')
#@connected_person_decorator
def sample_list_view (request):
	person = connected_user(request.user)
	samples = Sample.objects.filter()
	samples_count = samples.count
	users_count = Person.objects.count()
	print(person)
	return render (request, 'home/sample_list.html', locals()) 

@login_required (login_url = '/login/')
def sample_add_view (request):
	p, sample = None, None 
	if request.method == 'POST':
		form = sample_add_form(request.POST, request.FILES)
		if form.is_valid():
			p = Person.objects.get(user = request.user)
			sample = form.save(commit=False)
			sample.person = p
			sample.save()
			messages.success(request, 'Muestra agregada satisfactoriamente')

	
	form = sample_add_form()
	return render (request, 'home/sample_add.html', locals())

@login_required (login_url = '/login/')
def sample_detail_view(request, id_sample):
	sample = Sample.objects.get(id = id_sample)
	return render(request, 'home/sample_detail.html',locals()) 

@login_required (login_url = '/login/')
def sample_edit_view(request, id_sample):
	sample = Sample.objects.get(id = id_sample)
	if request.method == 'POST':
		form = sample_add_form(request.POST, request.FILES, instance=sample)
		if form.is_valid():
			sample = form.save(commit=False)
			sample.save()
			return redirect('/sample_detail/{}'.format(sample.id) )
	else:
		form = sample_add_form(instance=sample)
	return render(request, 'home/sample_edit.html',locals()) 

@login_required (login_url = '/login/')
def sample_delete_view (request, id_sample):
	sample = Sample.objects.get(id = id_sample)
	sample.delete()
	return redirect('/sample_list/')

