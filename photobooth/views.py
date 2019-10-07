from django.shortcuts import render
import datetime as dt
from .models import Image

# Create your views here.
def images_of_day(request):
    date =dt.date.today()
    photos=Image.objects.all()
    
    return render(request, "homepage.html",{"date":date,"photos":photos})


def image(request,img_id):
    try:
        pic=Image.get_img_by_id(img_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'image.html',{'pic':pic})