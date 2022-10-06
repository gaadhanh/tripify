num1=int(input("Enter a no"))
num2=int(input("Enter a no"))
num3=int(input("Enter a no"))
num4=int(input("Enter a no"))
if num1<num2 and num1<num3 and num1<num4:
    print(num1,"is smallest")
elif num2<num3 and num2<num4:
    print(num2, "is smalllest")
elif num3<num4:
    print(num3, "is smallest")    
else:
    print(num4, "is smallest")    