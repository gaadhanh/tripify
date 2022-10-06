class grandfather:
    def method1(self):
        print("Method 1 is working")
    def method2(self):
        print("Method 2 is working")

class father(grandfather):
    def method3(self):
        print("Method 3 is working")
    def method4(self):
        print("Method 4 is working")
    
class child(father):
    def method5(self):
        print("Method 5 is working")
    
g1=grandfather()
f1=father()
c1=child()

g1.method1()
f1.method2()
c1.method1()
c1.method4()

