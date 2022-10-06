try:
    a=open('hell.txt','r')
    print("file open..")
    f=a.read()
    print(f)
   
except FileNotFoundError:
    print("No such file found")
except TypeError as t:
    print(t)

finally:
    try:
        a.close()
        print("file closed")
    except NameError as n:
        print(n)
    


