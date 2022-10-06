uname=input("Enter the username")
pword=input("Enter the password")
l=len(pword)
n="0123456789"
if l>8 and pword[0] not in n:
    if "@" in pword or "#" in pword or "$" in pword:
        print("successfully logged in")
    else:
        print("invalid username and password")

else:
    print("invalid username and password")

