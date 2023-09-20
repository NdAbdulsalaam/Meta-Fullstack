from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Book

# Create your views here.

def index(request):
    return HttpResponse('My home')

def booking(request):
    my_books = Book.objects.all()
    return render(request, 'books.html', {'my_books': my_books})

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(title=title, author=author, price=price)
        
    try:
        book.save()
    except IntegrityError:
        return JsonResponse(
            {'error':'true','message':'required field missing'},status=400
        )
    
    return JsonResponse(model_to_dict(books), status=201)