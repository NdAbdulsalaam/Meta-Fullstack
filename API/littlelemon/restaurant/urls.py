from django.urls import path
from . import views

# SuperUsers
# Username: bistroadmin                                 facebook
# Email address: admin@littlelemon.com                  facebook@gmail.com
# Password: lemon@786!                                  facebook

urlpatterns = [
    path('', views.home, name="home"),
]