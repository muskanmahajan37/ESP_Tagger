from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf.urls.static import static
from django.conf import settings
import os


# Create your models here.
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    password = models.CharField(max_length=20)

    def __str__(self):
        return(self.user)



class Image(models.Model):

    p_image = models.ImageField(max_length=255,upload_to='p_image',default='NULL', blank='NULL')
    s_image1 = models.ImageField(max_length=255,upload_to='s_image')
    s_image2 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image3 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image4 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image5 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')

    
        

    

# @receiver(post_save, sender=Image)
# def update_file_path(instance, created, **kwargs):
#         if created:
#             initial_path = instance.s_image1.path
#             new_path = settings.MEDIA_ROOT + f'/s_image1_{instance.id}/{instance.s_image1.name}'
#             os.makedirs(os.path.dirname(new_path), exist_ok=True)
#             os.rename(initial_path, new_path)
#             instance.s_image1 = new_path
#             instance.save()

    

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return(self.username)

admin.site.register(Image)
admin.site.register(Score)
admin.site.register(Profile)
