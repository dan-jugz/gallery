from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/',default='')
