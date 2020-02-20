from django.db import models
from django.contrib.auth.models import User
import uuid

class List(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Wish(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(null=True,blank=True,max_length=200)
    image = models.ImageField(upload_to='wishes',null=True,blank=True)
    list = models.ForeignKey(List,on_delete=models.CASCADE,related_name="wishes")
    is_purchased=models.BooleanField(default=False)
    purchased_by=models.CharField(max_length=150)
