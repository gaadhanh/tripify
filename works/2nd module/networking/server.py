import socket

s=socket.socket()
s.bind(('192.168.180.252',5000))
print("Server running ............")
s.listen(2)
conn,add=s.accept()
print("Connection established by :",add)
data=conn.recv(1024).decode()
print(data)
s.close()


