from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
	    return self.title

class Human(models.Model):
    name = models.CharField(max_length=200)
    habit = models.TextField()