from django.conf.urls import url
from django.urls import path

from . import views
app_name ='pair'
urlpatterns = [
    url('', views.index, name='index'),
    url('/update', views.update_db, name='update_db'),

]
