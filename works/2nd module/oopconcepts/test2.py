from test import test

std1=test()
std1.name="Nandini"
std1.age=21
std1.place="Kottayam"
std1.pincode=686017

std2=test()
std2.name="Cerin"
std2.age=21
std2.place="Kumarakom"
std2.pincode=686563

std3=test()
std3.name="Sekhar"
std3.age="22"
std3.place="Trivandrum"
std3.pincode=686001

li=[std1,std2,std3]

for i in li:
    print(i.name,i.age,i.place,i.pincode)