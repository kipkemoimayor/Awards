from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/')
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    link=models.CharField(max_length=60)


class Profile(models.Model):
    profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
