from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .models import Image, Profile , answers, temp
import random
# Create your views here.
def index(request):
    
    if request.method == "POST" :
        user = request.POST.get("user")
        p_img = request.POST.get("p_img")
        ans = request.POST.get("ans")

    
        y = Image.objects.get(p_img=p_img).id
        y=y-8
        
        
        Profile.objects.create(user=user, p_img_id=y, p_ans=ans)
        y= random.randint(0,10)
        print("SEE 1st",request.method)
        
    
    else:

        user=request.user.id
        if len(temp.objects.all())!=0 and not temp.objects.filter(user=user).exists():
            p_id=temp.objects.all()[0].p_img_id
            temp.objects.filter(p_img_id=p_id).delete()
            s_img = answers.objects.get(p_img_id=p_id).ans_arr.split(' ')
            if request.method == "POST" :
                user = request.POST.get("user")
                p_img = request.POST.get("p_img")
                ans = request.POST.get("ans")

            
                y = Image.objects.get(p_img=p_img).id
                y=y-8
                
                Profile.objects.create(user=user, p_img_id=y, p_ans=ans)
                
                u_id = temp.objects.all()[0].user
                if Profile.objects.get(user=user).p_ans == Profile.objects.get(user=u_id).p_ans :
                    for u in (user,u_id):
                        Score.objects.create(user=u)
                        Score.objects.get(user=u).points += 1
                        Score.objects.get(user=u).save()

                    

                return HttpResponse('valid')
        
        else:

            for i in range(0,10):
                pass 
            y = random.randint(0,10)
            p = Image.objects.all()[y]
            
            count = p.p_img_count
            
            temp.objects.create(user=user, p_img_id=p.id)


            lst = [p.s_image1, p.s_image2, p.s_image3, p.s_image3, p.s_image4, p.s_image5]
            tmp =[]
            for i in range(0,3):
                px = Image.objects.all()[random.randint(0,14)]
                tmps=[px.s_image1, px.s_image2, px.s_image3, px.s_image3, px.s_image4, px.s_image5]
                tmp.append(tmps[random.randint(0,4)])
            
            x = random.randint(0,4)
            s_img = [lst[x]] + tmp
            random.shuffle(s_img)
            s = ' '.join(str(s_img))
            
            answers.objects.create(p_img_id=p.id, ans_arr = s)
            print("SEE ans array added",request.method)
            

            return render(request,'index.html',{"p_img":p, "s_img": s_img, 'media_url':settings.MEDIA_URL})






def update_db(request):

    print('HI')
    # username = request.user.username
    if request.method == POST :
        user = request.POST.get("user")
        p_img = request.POST.get("p_img")
        ans = request.POST.get("ans")

    
    y = Image.objects.get(p_img=p_img).id
    y=y-8
    
    
    Profile.objects.create(user=user, p_img_id=y, p_ans=ans)

    return redirect('/')