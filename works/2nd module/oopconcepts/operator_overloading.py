class gaa:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__(obj1,obj2):
        s1=obj1.a+obj1.b
        s2=obj2.a+obj2.b
        t=s1<s2
        return t

    def __str__(self):
        return '{} {}'.format(self.a,self.b)


obj1=gaa(9,4)
obj2=gaa(6,3)


print(obj1)



