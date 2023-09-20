from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    return HttpResponse('My home')

def books(request):
    my_books = Book.objects.all()
    # HttpResponse({'my_books': my_books})
    return render(request, 'books.html', {'my_books': my_books})