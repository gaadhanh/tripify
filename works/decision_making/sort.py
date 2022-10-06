a="python43obj5ct6ab2cd"
al=list(a)
n="1234567890"
li=[]
st=""
for i in a:
    if i in n:
        li.append(i)
        al.remove(i)
li.sort()
al.extend(li)  
for i in al:
    st=st+i
print(st)



