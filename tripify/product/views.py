from django.shortcuts import render,redirect
from .models import TravelPlace,commemnt

def details(request):
    id=request.GET['id']
    pro=TravelPlace.objects.get(id=id)
    cmt=commemnt.objects.filter(place_id=id)
    print(pro)
    return render(request,'single.html',{'pro':pro,'cmt':cmt})

def commenting(request):
    msg=request.GET['msg']
    pro_id=request.GET['pro_id']
    user=request.GET['user']
    cmt=commemnt.objects.create(cmt=msg,name=user,place_id=pro_id)
    cmt.save();
    return redirect('/')