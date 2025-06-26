from django.db import models
# Create your models here.
class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    resume = models.FileField(upload_to='media/')
    photo = models.ImageField(upload_to='media/')
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    
class CompanyRegistration(models.Model):
    namecompany = models.CharField(max_length=50) 
    gstid = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    comapanytype = models.CharField(max_length=50) 
    logo = models.ImageField()

