from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import TravelPlace
from django.contrib.auth.models import User,auth
from django.http import JsonResponse



def samp(request):
    #cookies viewing
    if 'name' in request.COOKIES:
        msg=request.COOKIES['name']
    else:
        msg="What say our clients"  

    #searching
    if request.method=="POST":
        val=request.POST['searchdestination']
        data=TravelPlace.objects.filter(name__istartswith=val)
    else:
        data=TravelPlace.objects.all()
    return render(request,"index.html",{'d':data,'msg':msg})


def lon(request):
    return render(request,"login.html")   


def reg(request):

    if request.method=="POST":
        
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pword=request.POST['pword']
        confpword=request.POST['confpword']
        ucheck=User.objects.filter(username=uname)
        echeck=User.objects.filter(email=email)
        if ucheck:
            msg="Username already exixts"
            return render(request,'register.html',{'msg':msg})

        elif echeck:
            msg="Email already exists"
            return render(request,'register.html',{'msg':msg})
        elif pword!=confpword:
            msg="Password donot match"
            return render(request,'register.html',{'msg':msg})
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pword)
            user.save();
            return redirect("/")
    else:        
        return render(request,"register.html")

def loginsub(request):
    if request.method=='POST':
       
        uname=request.POST['uname']
        pname=request.POST['pword']
        user=auth.authenticate(username=uname,password=pname)
        if user is not None:
            auth.login(request,user)
            res=redirect('/')
            res.set_cookie('name',uname)
            return res
        else:
            return render(request,'login.html',{'msg':'invalid username and password'})
    else:
        return render(request,'login.html')

def search(request):
    sch=request.POST['searchdestination']
    obj=TravelPlace.objects.filter(name__istartswith=sch)
    print(obj)
    return render(request,'test.html',{'s':sch})  

def logout(request):
    auth.logout(request)
    res= redirect('/')
    res.delete_cookie('name')
    return res
    


