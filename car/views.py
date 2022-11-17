from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def carshowroom(request):
    return HttpResponse ("Добро пожаловать в мир Mersedes")

#Car.objects.filter(id__gt=5)