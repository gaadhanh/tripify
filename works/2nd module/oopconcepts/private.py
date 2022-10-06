class private:
    def __init__(self,a,b):
        self.__a=a
        self._b=b
    
    def add(self):
        print(self.__a+self._b)
        

p=private(4,1)
p.add()


    