from django.core.exceptions import PermissionDenied

from .models import *

def connected_person_decorator(funcion):
	
	def connected(request, persona, *args, **kwargs):
		persona = Person.objects.get(user = request.user)
		try:
			persona = Person.objects.get(user = request.user)
			print ("xxxxxxxxxxxxxxxxxxxxx")
			print (persona.rol)
			print ("xxxxxxxxxxxxxxxxxxxxx")
			if persona.rol!='instructor':
				raise PermissionDenied
				
		except:
			pass
		return funcion(request, persona, *args, **kwargs) 
	return connected
