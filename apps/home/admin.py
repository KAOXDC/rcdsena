from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Rol)
admin.site.register(Person)
admin.site.register(Type)
admin.site.register(Component)
admin.site.register(Origin)
admin.site.register(Sample)
# course section 
admin.site.register(Area)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Person_Course)

