from count import count
from check import check


def username():
    
    uname=input("enter the username: ")
    pword=input("enter the password: ")
    place=input("enter place: ")
    if not check(uname):
        n=count()
        a=open('User_details/user'+n+'.txt','a')
        a.write(uname+'\n'+pword+'\n'+place)

username()   