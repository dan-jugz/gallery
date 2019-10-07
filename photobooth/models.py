from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/',default='')

    def __str__(self):
        return f'Image{self.title}-{self.img_loc}-{self.img_category}-{self.pub_date}'
    

class User(models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name
