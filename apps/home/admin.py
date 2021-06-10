from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(Type)
admin.site.register(Component)
admin.site.register(Origin)
admin.site.register(Sample)


