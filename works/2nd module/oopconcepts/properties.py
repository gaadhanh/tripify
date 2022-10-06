class student:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def display(self):
        print(self.name,self.age,self.place)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
       self._name=name.capitalize()


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        if age>20:
            self._age=20
        else:
            self._age=age


st1=student("gaadha",21,"Vazhoor")
st2=student("nandini",23,"Kottayam")
st3=student("cerin",16,"Kumarakom")
st4=student("sekhar",17,"Trivandrum")
st1.display()
st2.display()
st3.display()
st4.display()

