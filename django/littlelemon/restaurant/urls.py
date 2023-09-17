from django.urls import path
from . import views

# SuperUsers
# Username: bistroadmin                                 facebook
# Email address: admin@littlelemon.com                  facebook@gmail.com
# Password: lemon@786!                                  facebook

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_items, name="menu_items"),
]