a=open('username.txt','r')
f=a.readlines()
name=input("Enter the username")

if name+'\n' in f:
    print("username already there")
else:
    a=open('username.txt','a')
    a.write(name+'\n')
    
a.close()





  


