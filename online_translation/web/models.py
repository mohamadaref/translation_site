from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime


class Client(models.User):
    UserName = User.username()
    FirstName = User.first_name()
    LastName = User.last_name()
    Password = User.password()
    def __str__(self):
        return self.User_Name

class Translator(models.Model):
    UserName = User.username()
    FirstName = User.first_name()
    LastName = User.last_name()
    Password = User.password()
    CardNum = models.IntegerField(blank = False , null = False , default=0)
    PhoneNumber = models.CharField(max_length = 11 , blank = False , default = '')
    def __str__(self):
        return self.User_Name

class Documents(models.Model):
    UploadDate = models.DateTimeField(auto_now_add=True)
    # Done_date = models.DateField()
    # intended_date = models.IntegerField()
    TranslatorIs = models.OneToOneField(Translator , on_delete = models.CASCADE , default = '')
    ClientIs = models.OneToOneField(Client , on_delete = models.CASCADE , default ='')
    Description = models.CharField(max_length=255, blank=True , default = '')
    Document = models.FileField(upload_to='documents/')
    def __str__(self):
        return str(self.client) + ' ' + str(self.translator) + ' ' + str(self.Upload_date) + ' ' + str(self.description)
    # Create your models here
