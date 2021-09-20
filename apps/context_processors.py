from apps.home.models import *

def person_data(request):
	try:
		person = Person.objects.get(user = request.user)
	except:
		person = Person()
	return person


def notificaciones_transferencia_moto(request):
	try:
		noti = Sample.objects.filter().count()
	except:
		noti = 0
	return noti	

def my_processor(request):
	context = { 'ctx_person':person_data(request),
				'ctx_notificaciones': notificaciones_transferencia_moto(request),
	}
	return context