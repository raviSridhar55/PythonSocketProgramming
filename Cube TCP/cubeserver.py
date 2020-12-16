import socket

s = socket.socket()
s.bind(('localhost', 9999))

s.listen(1)
print('server listening')
c, addr = s.accept()
print('connected with', addr)
d = c.recv(1024)
while(True):
    c.sendall(str(int(d.decode())**3).encode())
    d = c.recv(1024)
    if(d.decode().strip()=='stop'):
        break
s.close()