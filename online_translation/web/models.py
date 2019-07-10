from django.db import models
import datetime

class Client(models.Model):
    First_name = models.CharField(max_length = 20 , blank = False , null = False , default = '')
    Last_name = models.CharField(max_length = 20 , blank = False , null = False , default = '')
    User_name = models.CharField(max_length = 30 , blank = False , null = False , default = '' , unique = True)
    Password = models.CharField(max_length = 20, blank = False , null = False , default = '')
    def __str__(self):
        return self.User_name

class Translator(models.Model):
    First_name = models.CharField(max_length = 20 , blank = False , null = False , default = '')
    Last_name = models.CharField(max_length = 20 , blank = False , null = False , default = '')
    User_name = models.CharField(max_length = 30 , blank = False , null = False , default = '' , unique = True)
    Password = models.CharField(max_length = 20, blank = False , null = False , default = '')
    Card_num = models.IntegerField(blank = False , null = False , default=0)
    def __str__(self):
        return self.User_name

class Documents(models.Model):
    Upload_date = models.DateTimeField(auto_now_add=True)
    # Done_date = models.DateField()
    # intended_date = models.IntegerField()
    translator = models.OneToOneField(Translator , on_delete = models.CASCADE , default = '')
    client = models.OneToOneField(Client , on_delete = models.CASCADE , default ='')
    description = models.CharField(max_length=255, blank=True , default = '')
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        return str(self.client) + ' ' + str(self.translator) + ' ' + str(self.Upload_date) + ' ' + str(self.description)
    # Create your models here
