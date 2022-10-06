import socket


s=socket.socket()
s.bind(('192.168.180.252',5000))
print("Server running ............")
s.listen(2)

while True:
    conn,add=s.accept()
    data=conn.recv(1024).decode()
    print(add,'::',data)
    b=input("Enter your message ")
    conn.send(bytes(b,'utf-8'))
    if data=="stop":
        break

s.close()
