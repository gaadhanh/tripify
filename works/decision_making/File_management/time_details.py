from count import count
import time
#from check import check


def username():
    x=count()
    uname=input("enter the name: ")
    prname=input("enter the product: ")
    a=open('date&time/product'+x+'.txt','a')
    a.write(uname+"/n"+prname+"/n"+time.localtime())

username()   