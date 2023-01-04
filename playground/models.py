from email.policy import default
from email.quoprimime import body_check
from enum import unique
from random import choices
from turtle import update
from uuid import uuid4
import uuid
from venv import create
from django.db import models
from django.forms import CharField

 
# creat your models here
class project(models.Model):
    #owner
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link = models.CharField(max_length=1000, null=True, blank=True )
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            img = self.featured_images.url
        except:
            img = ''
        return img

class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )        

#owner =
    project = models.ForeignKey(
        project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    update = models.DateTimeField(auto_now_add=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    
    def __str__(self):
       return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False) 

    def __str__(self):
        return self.name
                             