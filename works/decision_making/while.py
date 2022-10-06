li=[35,20,18,42,42,7,3,5,22,88,100,10,34]
l=len(li)
odd=[]
even=[]
i=0
while i<l:
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i])
    i=i+1
print(even)
print(odd)