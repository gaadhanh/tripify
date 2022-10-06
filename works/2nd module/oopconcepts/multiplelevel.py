class father:
    def method1(self):
        print("Method 1 is working")
    def method2(self):
        print("Method 2 is working")
    
class mother:
    def method3(self):
        print("Method 3 is working")
    def method4(self):
        print("Method 4 is working")

class child(father,mother):
    def method5(self):
        print("Method 5 is working")

f1=father()
m1=mother()
c1=child()

f1.method1()
m1.method3()
c1.method2()
c1.method4()

