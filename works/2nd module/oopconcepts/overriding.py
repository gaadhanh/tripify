class father:
    def phone(self):
        print("Samsung")

class child(father):
    def phone(self):
        print("Iphone")

f1=father()
c1=child()

c1.phone()