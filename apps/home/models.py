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
    ('aprendiz','Aprendiz'),
    ('instructor','Instructor'),
)

class Person(models.Model):
    """Model definition for Person."""

    document            = models.CharField(max_length = 10, unique = True)
    phone               = models.CharField(max_length = 20, null=True, blank= True)
    #photo               = models.ImageField(upload_to = 'persons', null=True, blank= True)
    email               = models.EmailField(unique=True)
    photo               = CloudinaryField(null=True, blank= True)
    rol                 = models.CharField(max_length = 15, choices = roles)
    user                = models.OneToOneField(User, models.PROTECT)

    class Meta:
        """Meta definition for Person."""

        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        return self.document + ' ' + self.rol + ' ' + self.user.username  + ' ' + self.user.email 

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
    #photo               = models.ImageField(upload_to = 'samples', null=True, blank= True)
    #demolition_object   = models.CharField(max_length = 50, choices = reasons)
    photo               = CloudinaryField('samples', null=True, blank= True)
    components          = models.ForeignKey(Component, models.PROTECT)
    origin              = models.ForeignKey(Origin, models.PROTECT)
    person              = models.ForeignKey(Person, models.PROTECT)

    class Meta:
        """Meta definition for Sample."""

        verbose_name = 'Muestra'
        verbose_name_plural = 'Muestras'

    def __str__(self):
        """Unicode representation of Sample."""
        return str(self.date_time) + ' ' + str(self.volume) + ' m3 ' + self.demolition_method + ' ' + str(self.person)
