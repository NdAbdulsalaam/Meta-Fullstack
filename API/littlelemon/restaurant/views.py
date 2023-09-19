from django.http import HttpResponse
from django.shortcuts import render
# from .forms import BookingForm
# from .models import Menu



# Create your views here.
def home(request):
    return HttpResponse("Start littlelemon book listing API")
    # return render(request, 'index.html')