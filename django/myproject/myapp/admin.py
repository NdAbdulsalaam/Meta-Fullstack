from django.contrib import admin
from . import models

# Register your models here.
myModels = [models.Booking, models.Menu]
admin.site.register(myModels)
