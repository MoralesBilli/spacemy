from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    saludo = "Hola Mundo"
    return HttpResponse(saludo)
