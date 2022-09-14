from django.shortcuts import render
from django.http import HttpResponse
from product.models import TravelPlace


def samp(request):
    data=TravelPlace.objects.all()
    return render(request,"index.html",{'d':data})

def lon(request):
    return render(request,"login.html")   

def reg(request):
    return render(request,"register.html")

def index(request):
    return render(request,'test.html')


