import socket

c = socket.socket()
c.connect(('localhost',9999))
print('client waiting')
while(True):
    command = input('enter number ')
    c.sendall(command.encode())
    msg = c.recv(1024)
    if(msg.decode()==''):
        break
    print('Server: '+msg.decode())
c.close()