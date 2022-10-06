
for i in range(7):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(6-i):
        print("*",end=" ")
    for j in range(7-i):
        print("*",end=" ")
    print()
for i in range(8):
    for j in range(7-i):
        print(' ',end=" ")
    for j in range(i+i+1):
        print('*',end=' ') 
    print()
