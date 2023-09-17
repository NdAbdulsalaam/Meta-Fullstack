from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    
    path('menu/', views.about, name="menu"),
    path('menu_item/', views.book, name="menu_item"),
]