def add(a,b):
    sum=a+b
    print(sum)

class testing:
    def add2(self,c,d):
        self.c=c
        self.d=d
        s=c+d
        print(s) 
    

t1=testing()
print(type(t1))
t1.add2(5,9)
t2=testing()
t2.add2(3,8)


add(4,7)
add(5,8)

print(t2.c)
print(t1.c)


