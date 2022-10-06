class protect:
    def __init__(self,a,b):
        self.a=a
        self._b=b

p=protect(7,3)

print(p._b)