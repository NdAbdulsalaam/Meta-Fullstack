from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='home'),
    # path('menu/<str:name>', views.menu, name='menu'),
    # path('members', views.members, name='members'),
    # path('booking/', views.form_view, name="booking"),
    path("employees/", views.employees, name = "employees")
]

