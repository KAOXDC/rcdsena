from apps.home.models import *

def person_data(request):
	try:
		person = Person.objects.get(user = request.user)
	except:
		person = Person()
	return person



def my_processor(request):
	context = { 'ctx_person':person_data(request),

	}
	return context