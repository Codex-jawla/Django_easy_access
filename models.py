from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=30)
    rollno = models.IntegerField(default=9999)
    branch = models.CharField(max_length=30,default="none")
    email = models.CharField(max_length=30,default="none",primary_key=True)
    phone = models.BigIntegerField(default=9999)