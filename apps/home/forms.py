from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import TextInput, Widget
from .models import *
from django.contrib.auth.models import User


class search_form (forms.Form):
	search = forms.CharField(
		label='Buscar Usuario ',
		required=False,
		widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':'Por nombre, apelllidos, No. identificacion'})
		)
class login_form (forms.Form):
	username    = forms.CharField(
		label = 'Usuario o Correo',
		widget=forms.TextInput(attrs={'class': 'form-control'})
		)
	password    = forms.CharField(
		label ='Clave',
		widget=forms.PasswordInput(attrs={'class': 'form-control'}, render_value=False))

class profile_form(forms.ModelForm):
	pass_1	    = forms.CharField(label= 'clave', required=False, widget=forms.PasswordInput(render_value=False))
	pass_2	    = forms.CharField(label= 'Confirmar Clave',  required=False, widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = User
		fields = '__all__'
		exclude =['last_login', 'groups', 'user_permissions', 'email', 'date_joined', 'password', 'is_superuser', 'is_staff', 'is_active']

	def __init__(self, *args, **kwargs):
		super(profile_form, self).__init__(*args, **kwargs)
		for field in self.fields:	
			self.fields[field].widget.attrs.update({'class': 'form-control'})

	def clean_user_name (self):
		user_name = self.cleaned_data['user_name']
		try:
			u = User.objects.get(username = user_name)
		except User.DoesNotExist:
			return user_name 
		raise forms.ValidationError('Usuario ya registrado')

	def clean_pass_2 (self):
		pass_1 = self.cleaned_data['pass_1']
		pass_2 = self.cleaned_data['pass_2']
		if pass_1 == pass_2:
			pass
		else:
			raise forms.ValidationError('las Claves no coinciden')

class user_form(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name']
		exclude =['last_login', 'groups', 'user_permissions', 'email', 'date_joined', 'password', 'is_superuser', 'is_staff', 'is_active']
		labels={
				'first_name':'Nombres',
				'last_name':'Apellidos',
		}
	def __init__(self, *args, **kwargs):
		super(user_form, self).__init__(*args, **kwargs)
		for field in self.fields:	
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class person_form(forms.ModelForm):

	class Meta:
		model = Person 
		fields = [ 'document', 'email', 'phone', 'rol', 'photo' ]
		exclude = ['user',]
		labels={
				'document':'No. de Identificacion',
				'email':'Correo',
				'phone':'Celular',
				'rol':'Rol',
				'photo':'Foto',
		}
	def __init__(self, *args, **kwargs):
		super(person_form, self).__init__(*args, **kwargs)
		for field in self.fields:	
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class sample_add_form (forms.ModelForm):
	class Meta:
		model = Sample
		fields = '__all__'
		exclude = ['person', ]

	def __init__(self, *args, **kwargs):
		super(sample_add_form, self).__init__(*args, **kwargs)
		for field in self.fields:	
			self.fields[field].widget.attrs.update({'class': 'form-control'})


