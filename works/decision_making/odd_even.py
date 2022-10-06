li=[35,20,18,42,42,7,3,5,22,88,100,10]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)