from django.db import models

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  #host = 
  #topic = 
  #participants = 

  def __str__(self):
    return str(self.name)
  

  ## serve para retornar o nome da sala ao instanciar no banco de dados
  # ao inves de retornar o objeto, retornara a string