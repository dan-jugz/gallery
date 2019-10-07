from django.db import models
import datetime as dt


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name


class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    img_loc = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    img_category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/',default='')

    def __str__(self):
        return f'Image{self.title}-{self.img_loc}-{self.img_category}-{self.pub_date}'
    