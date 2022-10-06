a=input("enter a no")
l=len(a)
s="0123456789"
for i in range(l):
    if a[i] in s and "." not in a:
        f=0
    else:
        z=".0123456789"
        for i in range(l):
            if a[i] in z:
                f=1
            else:
                f=2
                break
if f==1:
    print("float")
elif f==0:
    print("int")
else:
    print("string")

     