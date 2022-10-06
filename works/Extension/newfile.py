import os
path=r"C:\Users\ganes\Desktop\Further_Extension"
li=os.listdir(path)

for i in  li:
    print(os.path.splitext(i)[1])
    
    