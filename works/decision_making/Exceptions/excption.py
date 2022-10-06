from logging import exception


try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print(a/1)
except ValueError as vler:
    print(vler)
except:
    print("Error occured")

print("second work")