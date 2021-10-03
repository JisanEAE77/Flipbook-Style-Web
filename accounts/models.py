from django.db import models
from django.contrib.auth.models import User, AbstractUser
from bookstore.models import *

# Create your models here.

class Library(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Book, related_name="bookcart", blank= True)
    wishlist = models.ManyToManyField(Book, related_name="wishbook", blank= True)
    subsciption = models.CharField(max_length=20)
    owned = models.ManyToManyField(Book, related_name="mybook", blank= True)

    def __str__(self):
        return str(self.username)
