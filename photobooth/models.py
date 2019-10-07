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
    