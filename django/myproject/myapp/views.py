from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def menu(request, name):
    fruits = {
        'lemon': 'Lemon is a type of fruit',
        'apple': 'Apple is a type of fruit',
        'banana': 'Banana is a type of fruit',
        'orange': 'Orange is a type of fruit'
    }
    
    description = fruits[name]
    
    return HttpResponse(f"<h2>{name}</h2> {description}")

