import re

a=open(r'C:\Users\ganes\Desktop\works\vedio.txt','r')
val=a.read()

st=""
value=re.findall("[a-z]",val)
v=set(value)
li=list(v)
li.sort()
for i in li:
    st+=i
print(st)
    
ct=""
caps=re.findall("[A-Z]",val)
c=set(caps)
l=list(c)
l.sort()
for i in l:
    ct+=i
print(ct)

nt=""
num=re.findall("[0-9]",val)
n=set(num)
lis=list(n)
lis.sort()
for i in lis:
    nt+=i
print(nt)
