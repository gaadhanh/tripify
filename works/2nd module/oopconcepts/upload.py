name=input("Enter name: ")
no=input("Enter number: ")
m1=int(input("Enter physics marks: "))
m2=int(input("Enter chemistry marks: "))
m3=int(input("Enter maths marks: "))

f=open('teachers2.py','a')
f.write(f'''{no}=exam_result()
{no}.upload('{name}','{no}',{m1},{m2},{m3})
''')
f.close()


