from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Friend(models.Model):
	users = models.ManyToManyField(User)