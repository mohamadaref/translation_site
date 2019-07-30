from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.conf import settings
import datetime

class CustomUser(AbstractUser,models.Model):
    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').null = False
    ProfileImage = models.ImageField(blank = True , upload_to='profile_img/', default = 'profile_img/no-img.jpg')
    def __str__(self):
        return self.username

class Client(models.Model):
    User = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True, related_name='client_profile' , unique = True)
    def __str__(self):
        return self.User.username

class Translator(models.Model):
    User = models.OneToOneField(CustomUser,on_delete=models.CASCADE, null=True, related_name='translator_profile' , unique = True)
    CardNum = models.IntegerField(blank = False , null = True , default=0 , unique = True)
    PhoneNumber = models.CharField(max_length = 11 , blank = False , default = '' , null = True , unique = True)
    def __str__(self):
        return self.User.username

class Document(models.Model):
    UploadDate = models.DateTimeField(auto_now_add=True)
    TranslatorIs = models.OneToOneField(Translator , on_delete = models.CASCADE , default = '')
    ClientIs = models.OneToOneField(Client , on_delete = models.CASCADE , default ='')
    Description = models.CharField(max_length=255, blank=True , default = '')
    Document = models.FileField(upload_to='documents/')
    def __str__(self):
        return str(self.ClientIs) + ' ' + str(self.TranslatorIs) + ' ' + str(self.UploadDate) + ' ' + str(self.Description)
    # Create your models here
