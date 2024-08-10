from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

class Intereses(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    picture = models.ImageField(upload_to='imagen_del_perfil/',null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    pais = CountryField(blank=True,null=True)
    age = models.IntegerField()
    intereses = models.ManyToManyField('Intereses', blank=True)

    def __str__(self):
        return self.user
    
    