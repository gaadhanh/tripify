class case:
    def __init__(self,b):
        self.b=b
    def low(self):
        print(self.b.lower())
    def upp(self):
        print(self.b.upper())
    
ob1=case("Hey")
ob1.low()
ob1.upp()

li=int(5)
print(type(li))
li2=case("hey")
print(type(li2))

