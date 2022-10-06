class capital:
    def __init__(self,str):
        self.str=str
    def cap(self):
        s=self.str[0].upper()
        st=self.str[1:len(self.str)]
        print(s+st)
            

c1=capital("helloo")
c1.cap()

