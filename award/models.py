from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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
    date=models.DateField(auto_now=True)


class Profile(models.Model):
    profile=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()

class Rates(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0)
    content=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)
