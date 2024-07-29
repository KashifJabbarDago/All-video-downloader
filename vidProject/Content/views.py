from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.

def Home(request):
    print("Home working")
    return render(request,"Home.html")

def performTask(request):
    
    return render(request,"templates/Home.html")

def youtubeDownload(request):
    return render(request,"youtubeDownload.html")

def facebookDownload(request):
    return HttpResponse("Facebook downloading")

def instagramDownload(request):
    return HttpResponse("instagram Downloading")

