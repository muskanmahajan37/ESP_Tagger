from django.shortcuts import render
from django.conf import settings
from .models import Image, Profile
import random
# Create your views here.
def index(request):
    y= random.randint(0,10)
    # p = Image.objects.all()[y]
    # if (p):
    #     print("true")
    #     # p_img = Image.objects.all()[y]
    #     #Image.objects.all()[y].p_image_count += 1

    #     p_img = Image.objects.all()[y].save()
    #     p_img = Image.objects.all()[y]

    # lst = [p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
    # x = random.randint(0,4)
    # tmp =[]
    # for i in range(0,3):
    #     p = Image.objects.all()[random.randint(0,14)]
    #     tmps=[p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
    #     tmp.append(tmps[random.randint(0,4)])
        
    

    # s_img = [lst[x]]+ tmp
    # random.shuffle(s_img)

    for i in range(0,10):
        pass 
    p = Image.objects.all()[y]
    count = p.p_img_count
    lst = [p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
    tmp =[]
    for i in range(0,3):
        p = Image.objects.all()[random.randint(0,14)]
        tmps=[p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
        tmp.append(tmps[random.randint(0,4)])
    
    x = random.randint(0,4)
    s_img = [lst[x]] + tmp
    random.shuffle(s_img)
    print('hey')

    return render(request,'index.html',{"p_img":p, "s_img": s_img, 'media_url':settings.MEDIA_URL})

def update_db(request):

    print('HI')
    # username = request.user.username
    user = request.GET.get("user")
    p_img = request.GET.get("p_img")
    ans = request.POST.get("ans")

    
    y = Image.objects.get(p_img=p_img).id
    y=y-8
    
    
    Profile.objects.create(user=user, p_img_id=y, p_ans=ans)
    #should update but not because a is a string .. should be only a field name type.
    

    # print(p,username, "p")
    return render(request, 'index.html', {})