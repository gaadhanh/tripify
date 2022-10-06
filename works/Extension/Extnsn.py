import os
path=r"C:\Users\ganes\Desktop"
li=os.listdir(path)
for i in li:
    j=i.split('.')
    if 'jpg' in j:
        print
        