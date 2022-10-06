def check(name):
    a=open('count.txt','r')
    f=a.read()
    li=[]
    for i in range(int(f)):
        a=open(f'User_details/user{str(i)}.txt','r')
        li.append(a.readlines()[0])
    return name+'\n' in li
       

        