import socket

s=socket.socket()
s.bind(('localhost',9999))
s.listen(1)
print('Server is listening')
c, addr = s.accept()
print('Connected with ', addr)
while(True):
    d=c.recv(1024)
    if(d.decode()=="stop"):
        c.sendall(d)
        print("Stopping connection")
        break
    print('client:', d.decode())
    c.sendall(d)
s.close()