from django.db import models
from django.contrib import admin
# Create your models here.
class Image(models.Model):
    p_image = models.ImageField(max_length=255,upload_to='p_image',default='NULL', blank='NULL')


admin.site.register(Image)