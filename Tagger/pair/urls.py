from django.conf.urls import url
from django.urls import path

from . import views
app_name ='pair'

urlpatterns = [
    url('update1/', views.update_db, name='update_db'),
    url('', views.index, name='index'),
    

]
