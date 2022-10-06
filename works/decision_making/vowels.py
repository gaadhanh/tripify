name=input("Enter a name")
l=len(name)
if l%2==0:
    if name[0]=="A" or name[0]=="a" or name[0]=='E' or name[0]=="e" or name[0]=="I" or name[0]=="i" or name[0]=="O" or name[0]=="o" or name[0]=="U" or name[0]=="u":
        print(name[0])
    else:
        print("invalid")

else:
    print(name[-1])

