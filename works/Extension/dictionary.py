import os
path=r"C:\Users\ganes\Desktop\Further_Extension"

l=[]
li=os.listdir(path)
for i in li:
    w=i.split('.')
    l.append(w[1])
print(l)
s=set(l)
print(s)
dic={}
for j in s:
    dic[j]=l.count(j)
print(dic)




        


