class parent:
    def method1(self):
        print("method 1 is working")
    def method2(self):
        print("method 2 is working")
    
class child(parent):
    def method3(self):
        print("method 3 is working")
    
ob1=parent()
ob2=child()

ob1.method1()
ob2.method2()
