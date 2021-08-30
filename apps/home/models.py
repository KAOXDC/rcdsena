from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from cloudinary.models import CloudinaryField


methods = (
    ('mecanica', 'Mecanica'),
    ('manual', 'Manual'),
)
origins = (
    ('columna', 'Columna'),
    ('losa', 'Losa'),
    ('viga', 'Viga'),
)
reasons = (
    ('mejora','Mejora'),
    ('estructural','Estructural'),
)
roles = (
    ('registrado','Registrado'),
    ('administrador','Administrador'),
)

class Rol (models.Model):
    name    = models.CharField(max_length=200, unique=True)
    status  = models.BooleanField(default=True)
    type    = models.CharField(max_length=50, choices=roles, default='registrado')

    def __str__ (self):
        return self.name + ' --- ' + self.type 

class Person(models.Model):
    """Model definition for Person."""

    document            = models.CharField(max_length = 10, unique = True)
    phone               = models.CharField(max_length = 20, null=True, blank= True)
    #photo               = models.ImageField(upload_to = 'persons', null=True, blank= True)
    email               = models.EmailField(unique=True)
    photo               = CloudinaryField(null=True, blank= True)
    rol                 = models.ForeignKey(Rol, on_delete = models.PROTECT)
    user                = models.OneToOneField(User, on_delete = models.PROTECT)

    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        return self.document + ' ' + self.rol.name + ' ' + self.user.username  + ' ' + self.user.email 

class Type(models.Model):
    """Model definition for Type."""

    name = models.CharField(max_length= 100)

    class Meta:
        """Meta definition for Type."""

        verbose_name = 'Tipo de componente'
        verbose_name_plural = 'Tipos de componentes'

    def __str__(self):
        """Unicode representation of Type."""
        return self.name

class Component(models.Model):
    """Model definition for Component."""

    name        = models.CharField(max_length= 100)
    type_name   = models.ForeignKey(Type, models.PROTECT)
    class Meta:
        """Meta definition for Component."""

        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'

    def __str__(self):
        """Unicode representation of Component."""
        return self.type_name.name + ' ' + self.name

class Origin(models.Model):
    """Model definition for Origin."""

    name        = models.CharField(max_length= 100)
    class Meta:
        """Meta definition for Origin."""

        verbose_name = 'Origen'
        verbose_name_plural = 'Origines'

    def __str__(self):
        """Unicode representation of Component."""
        return self.name

class Sample(models.Model):
    """Model definition for Sample."""
    date_time           = models.DateTimeField(auto_now_add = True) 
    volume              = models.DecimalField(max_digits = 6, decimal_places= 2)
    #demolition_method   = models.CharField(max_length = 50, choices = methods)
    #origin              = models.CharField(max_length = 50, choices = origins)
    #demolition_object   = models.CharField(max_length = 50, choices = reasons)
    #photo               = models.ImageField(upload_to = 'samples', null=True, blank= True)
    #document            = models.FileField(upload_to = 'documents', null=True, blank= True)
    # Phothos and Documents wil be adden in cloudinary temporary, until deploy this app to Cloud SENA Server
    photo               = CloudinaryField('samples', null=True, blank= True)
    document            = CloudinaryField('documents', null=True, blank= True)
    components          = models.ForeignKey(Component, models.PROTECT)
    origin              = models.ForeignKey(Origin, models.PROTECT)
    person              = models.ForeignKey(Person, models.PROTECT)

    class Meta:
        """Meta definition for Sample."""

        verbose_name = 'Residuo'
        verbose_name_plural = 'Residuos'

    def __str__(self):
        """Unicode representation of Sample."""
        return str(self.date_time) + ' ' + str(self.volume) + ' m3 ' + self.demolition_method + ' ' + str(self.person)

'''
Courses Area
'''
class Area (models.Model):
    name    = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Program (models.Model):
    name    = models.CharField(max_length=200)
    area    = models.ForeignKey(Area, on_delete=models.PROTECT)
    def __str__ (self):
        return self.name

class Course (models.Model):
    name            = models.CharField(max_length=200, unique=True)
    initial_date    = models.DateField(null=True, blank=True)
    final_date      = models.DateField(null=True, blank=True)
    status          = models.BooleanField(default=True)
    program         = models.ForeignKey(Program, on_delete=models.PROTECT)
        
    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'

    def __str__ (self):
        return self.name + ' ' + str(self.initial_date) + ' ' + str(self.status)

class Person_Course (models.Model):
    person = models.ForeignKey(Person, on_delete= models.PROTECT, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete= models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.person.user.first_name + ' ' + self.course.name


