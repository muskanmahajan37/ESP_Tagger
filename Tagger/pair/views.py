from django.shortcuts import render
from django.conf import settings
from .models import Image
import random
# Create your views here.
def index(request):
    y= random.randint(0,10)
    p = Image.objects.all()[y]
    if (p):
        print("true")
        # p_img = Image.objects.all()[y]
        #Image.objects.all()[y].p_image_count += 1

        p_img = Image.objects.all()[y].save()
        p_img = Image.objects.all()[y]

    lst = [p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
    x = random.randint(0,4)
    tmp =[]
    for i in range(0,3):
        p = Image.objects.all()[random.randint(0,14)]
        tmps=[p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
        tmp.append(tmps[random.randint(0,4)])
        
    

    s_img = [lst[x]]+ tmp
    random.shuffle(s_img)

    


    return render(request,'index.html',{"p_img":p_img, "s_img": s_img, 'media_url':settings.MEDIA_URL})