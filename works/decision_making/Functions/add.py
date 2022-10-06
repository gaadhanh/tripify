def add(num1,*num2):
    print(num1)
    print(num2)
    for i in num2:
        num1+=i
    print("Sum of values are",num1)
add(4,9,2,3,6,1)
