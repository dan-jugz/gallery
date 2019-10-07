from django.db import models
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class Location(models.Model):
    loc_name=models.CharField(max_length=100)

    def __str__(self):
        return self.loc_name

    # method to save location to database
    def save_loc(self):
        self.save()

    # method to delete a category from db  
    def delete_loc(self): 
        self.delete()


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    # method to save a category to db
    def save_category(self):
        self.save() 

    # method to delete a category from db
    def delete_category(self):
        self.delete()

class tags(models.Model):
    tag_name=models.CharField(max_length=30, default='tag_name')

    def __str__(self):
        return self.tag_name


class Image(models.Model):
    title = models.CharField(max_length =60)
    post = models.CharField(max_length =100)
    img_loc = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    img_category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return f'Image{self.title}-{self.img_loc}-{self.img_category}-{self.pub_date}'
    
    #Using lookup that spans relations to fetch for all photos with a searched keyword regardless of case
    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter( Q(img_category__category_name__iexact=search_term) | 
        Q(img_loc__loc_name__icontains=search_term) | Q(img_name__icontains=search_term)  | Q(author__first_name__icontains=search_term))
        return photos  

    # method that fetches photos with date published
    @classmethod
    def get_photos(cls):
        photos=cls.objects.order_by(pub_date__date = date)
        return photos


    @classmethod
    def filter_by_location(cls,location):
        photos=cls.objects.filter(img_loc__loc_name__icontains=location)
        return photos


    @classmethod
    def get_img_by_id(cls,img_id):
        pic=cls.objects.get(pk=img_id)
        return pic

    
    @classmethod
    def delete_photo():
        pass