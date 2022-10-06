class exam_result:
    
    def upload(self,name,no,m1,m2,m3):
        self.name=name
        self.no=no
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def result(self):
        print("Name: ",self.name)
        print("Roll Number: ",self.no)
        print("Physics: ",self.m1)
        print("Chemistry: ",self.m2)
        print("Maths: ",self.m3)
        print("Total: ",self.m1+self.m2+self.m3)
        print("Average: ",(self.m1+self.m2+self.m3)/3)
        print("\n##############################")


    