from django.shortcuts import render
from django.conf import settings
from .models import Image
import random
# Create your views here.
def index(request):
    y=0
    p_img = Image.objects.all()[y]
    x = random.randint(0,4)
    s_img = Image.objects.all()[x]


    return render(request,'index.html',{"p_img":p_img, 'media_url':settings.MEDIA_URL})