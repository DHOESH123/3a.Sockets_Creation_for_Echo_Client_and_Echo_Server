import socket
s=socket.socket()
s.bind(('localhost',8000))
s.listen(5)
c,addr=s.accept()
while True:
    clientmessage=c.recv(1024).decode()
    c.send(clientmessage.encode())
