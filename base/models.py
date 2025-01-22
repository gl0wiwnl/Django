from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


## model Room

class Room(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
  #participants = 

  def __str__(self):
    return str(self.name)  ## serve para retornar o nome da sala ao instanciar no banco de dados ao inves de retornar o objeto, retornara a string
  

 

class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) 
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self): 
      return str(self.body[0:50])