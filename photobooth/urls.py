from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.images_of_day,name='imagesToday'),
    url(r'^search/$',views.search_results,name='search_results'),
    url(r'^image/(\d+)',views.image,name='image')
]