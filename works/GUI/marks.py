name=input("Enter the name of student: ")
no=int(input("Entere the no of subjects: "))
li=[]
dic={}

for i in range(no):
    s=input("Enter the name of subject: ")
    li.append(s)
for i in li:
    print("Enter mark of",i,": ")
    mark=input()
    dic[i]=mark
print("#########################")
print("\nName: ",name)
for j in dic:
    print(j,":",dic[j])
mar=dic.values()
print("Maximum marks : ",max(mar))

tot=0
count=0
for i in mar:
    tot=tot+int(i)
    count=count+1
print("Total marks: ",tot)
print("Average marks obtained id: ",tot/count)

print("#########################")

