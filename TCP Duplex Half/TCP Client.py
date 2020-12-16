import socket
s = socket.socket()
s.connect(('localhost', 1234))
print('waiting for connection....')
s.sendall('Connected to client'.encode())
while (True):
    msg =  s.recv(1024)
    if (msg.decode() == 'exit'):
        print('connection ended')
        break
    # else:
    print(msg.decode())
    data = input('enter something..')
    s.sendall(data.encode())
    if (data == 'exit'):
        break
s.close()
