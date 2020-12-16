import socket

c = socket.socket()

c.connect(('localhost',9999))
print('Client waiting for connection')
c.sendall('Client Connected'.encode())
while(True):
    msg = c.recvfrom(1024)
    if (msg[0].decode() == ''):
        break
    print('Server:'+msg[0].decode())
    command = input("Enter command to continue or terminate: ")
    c.sendall(command.encode())
    if command == "stop":
        break
c.close()
