import socket

c=socket.socket()
c.connect(('192.168.180.252',5000))
print("Connected to server")
c.send(bytes("heyy goois",'utf-8'))
c.close()
