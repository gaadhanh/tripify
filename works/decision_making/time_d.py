import time
import os

name=input("Enter the name: ")
prname=input("Enter the product name: ")
n=len(os.listdir('File_management/date_time'))
a=open("File_management/date_time/product"+str(n),'w')
a.write(name+'\n'+prname+'\n'+time.ctime())
a.close()

