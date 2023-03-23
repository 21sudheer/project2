from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Emp(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(null=True)
    username=models.CharField(max_length=255,null=True)
    

    def __str__(self):
        return self.firstname

    



