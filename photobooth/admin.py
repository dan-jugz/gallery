from django.contrib import admin
from .models import Location,Category,Image,tags,User

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)
