from django.shortcuts import render
from django.http import HttpResponse
from .models import product


def samp(request):
    return render(request,"index.html")

def lon(request):
    return render(request,"login.html")   

def reg(request):
    return render(request,"register.html")


p1=product()
p1.name="Toblerone"
p1.price=175
p1.dsc="Swiss chocolate with distinctive shape known for its unique taste."

p2=product()
p2.name="Galaxy"
p2.price=70
p2.dsc="Chocolate bar made and marketed by mars.Inc"

p3=product()
p3.name="Munch"
p3.price=10
p3.dsc="Nestle munch is the country's most loved coated wafers."

p4=product()
p4.name="Snickers"
p4.price=35
p4.dsc="Sweet and salty chocolate bar filled with nuts and dry fruits."

pro=[p1,p2,p3,p4]

def index(request):
    return render(request,'test.html',{'a':pro})


