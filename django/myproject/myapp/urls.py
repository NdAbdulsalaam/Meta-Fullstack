from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('menu/<str:name>', views.menu, name='menu')
]

