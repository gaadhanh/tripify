#student data inserting

num=int(input("Enter the no of students: "))
top=[]
li=[]
for i in range(num):
    t=[]
    t.append(input("Enter the name of students: "))
    t.append(int(input("Enter mark of first sub: ")))
    t.append(int(input("Enter mark of second subject: ")))
    t.append(int(input("Enter mark of third subjec: ")))
    t.append(t[1]+t[2]+t[3])
    top.append(t[1]+t[2]+t[3])
    t.append(t[4]/3)
    li.append(t)


#displaying values

for i in li:
    print("Name: ",i[0])
    print("Mark in English: ",i[1])
    print("Mark in Malayalam: ",i[2])
    print("Mark in Maths: ",i[3])
    print("Total marks: ",i[4])
    print("Average marks: ",i[5])
    print("\n################################\n")

print("\n################################\n")
print("Toppest mark: ",max(top))

    