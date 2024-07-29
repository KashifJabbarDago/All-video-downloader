from django.conf import urls
from django.urls import path 
from . import views
urlpatterns=[
    path('',views.Home,name="Home"),
    path('/perform',views.performTask,name="performTask"),
    path('/youtubeDownload',views.youtubeDownload,name="youtubeDownload"),
    path('/facebookDownload',views.facebookDownload,name="facebookDownload"),
    path('/instagramDownload',views.instagramDownload,name="instagramDownload")

]