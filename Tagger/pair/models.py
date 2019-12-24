from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
 
class Profile(models.Model):
    user = models.CharField(max_length=255, default='NA')
    p_img_id = models.IntegerField()
    p_ans = models.CharField(max_length=1000)

    
# model
# register page
# p_img 


class Image(models.Model):

    p_img = models.ImageField(max_length=255,upload_to='p_image',default='NULL', blank='NULL')
    p_img_count = models.IntegerField(default=0)

    s_image1 = models.ImageField(max_length=255,upload_to='s_image')
    s_image2 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image3 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image4 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    s_image5 = models.ImageField(max_length=255,upload_to='s_image',default='NULL', blank='NULL')
    

    def __str__(self):
        return(str(self.p_img))


    

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return(self.username)

class answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ans_arr = models.CharField(max_length=1000)

admin.site.register(Image)
admin.site.register(Score)
admin.site.register(Profile)
admin.site.register(answers)

