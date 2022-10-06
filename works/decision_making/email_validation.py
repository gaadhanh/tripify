email=input("Enter the email id")
if "@gmail" in email and "@" not in email[0:4]:
    if ".com" in email or ".edu" in email or ".in" in email:
        print("valid")
    else:
        print("invalid")

else:
    print("invalid")