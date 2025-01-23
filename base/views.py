from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# rooms = [
#   {'id': 1, 'name': 'Lets Learn python!'},
#   {'id': 2, 'name': 'Design with me'},
#   {'id': 3, 'name': 'Frontend Developers'},

# ]


def home(request, ):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request, 'base/home.html', context)

def room(request, pk): 
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request, 'base/room.html', context)

def createRoom(request):
  form = RoomForm()
  print(request.method)
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      print(form.errors)

  context = {'form': form}
  return render(request, 'base/room-form.html', context)