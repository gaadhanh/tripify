import socket

c=socket.socket()
c.connect(('192.168.180.253',5000))
print("Connected to server")

a=input("Enter your message ")
c.send(bytes(a,'utf-8'))
c.close()
