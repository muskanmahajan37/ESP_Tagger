from django.shortcuts import render
from django.conf import settings
from .models import Image
# Create your views here.
def index(request):
    img = Image.objects.all()[0]
    return render(request,'index.html',{"img":img, 'media_url':settings.MEDIA_URL})