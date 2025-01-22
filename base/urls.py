from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
  path('', views.Home, name='home'),
  path('room/<str:pk>/', views.room, name='room'),
]