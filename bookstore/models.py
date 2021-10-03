from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
from dateutil.parser import parse
import maya
from ckeditor.fields import RichTextField

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    pdf = models.FileField(upload_to='bookspdf', blank=False)
    thumbnail = models.ImageField(upload_to='booksthumb', blank=False)

    def __str__(self):
        return self.name + " - $" + str(self.price)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='blogimage', blank=False)
    thumbnail = models.ImageField(upload_to='blogthumb', blank=False)
    time = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        date_time_str = str(self.time)
        date_time_obj = maya.parse(date_time_str).datetime()
        return (self.title + " - " + str(date_time_obj.date()) + ", " + str(date_time_obj.time().strftime("%I:%M %p")) + ", " + str(date_time_obj.tzinfo))


class Subscription(models.Model):
    plan_name = models.CharField(max_length=50)
    per = models.CharField(max_length=50)
    price = models.FloatField()
    days = models.BigIntegerField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.plan_name + " - " + str(self.price)