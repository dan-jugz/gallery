from django.shortcuts import render
import datetime as dt
from .models import Image

# Create your views here.
def images_of_day(request):
    date =dt.date.today()
    photos=Image.objects.all()
    
    return render(request, "homepage.html",{"date":date,"photos":photos})
