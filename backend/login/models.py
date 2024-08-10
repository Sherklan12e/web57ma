from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True)
    picture = models.ImageField(upload_to='imagen_del_perfil/',null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    
    