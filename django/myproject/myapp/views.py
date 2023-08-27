from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")

def members(request):
    pass

def menu(request, name):
    fruits = {
        'lemon': 'Lemon is a type of fruit',
        'apple': 'Apple is a type of fruit',
        'banana': 'Banana is a type of fruit',
        'orange': 'Orange is a type of fruit'
    }
    
    description = fruits[name]
    
    return HttpResponse(f"<h2>{name}</h2> {description}")

def form_view(request):
    forms = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print("Saved!")
    context = {"form" : forms}
    return render(request, "booking.html", context)




