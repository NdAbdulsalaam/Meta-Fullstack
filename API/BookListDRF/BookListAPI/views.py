from django.shortcuts import render

# These are used in the test view for my first API
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# These are used for the serializer
from . import models, serializer
from rest_framework import generics

# Create your views here.

# Just test view when creating my first API
@api_view()
def books(request):
    return Response("Not sure of what i'm doing yet", 
                    status=status.HTTP_200_OK)
    
class BookView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializer.MenuItemSerializer
    
class CategoriesView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializer.MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['category']