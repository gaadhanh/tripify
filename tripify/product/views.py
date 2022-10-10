from django.shortcuts import render,redirect
from .models import TravelPlace,commemnt
from django.core.cache import cache

def details(request):

    id=request.GET['id']
    if cache.get(id):
        pro=cache.get(id)
        print('data from cache')
           
    else:
        pro=TravelPlace.objects.get(id=id)
        cache.set(id,pro)
        print('data from database')
         
    cmt=commemnt.objects.filter(place_id=id)
    print(pro)
    res=render(request,'single.html',{'pro':pro,'cmt':cmt})
    res.set_cookie('pro_name',pro.name)
    return res
    

def commenting(request):
    msg=request.GET['msg']
    pro_id=request.GET['pro_id']
    user=request.GET['user']
    cmt=commemnt.objects.create(cmt=msg,name=user,place_id=pro_id)
    cmt.save();
    return redirect('/')

