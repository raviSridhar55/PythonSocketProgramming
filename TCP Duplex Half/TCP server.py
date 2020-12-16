import socket
s = socket.socket()
s.bind(('localhost',1234))
s.listen(5)
print('server is listining')
c, add = s.accept()
print('connected to..', add)
d = c.recv(1024)
ms = 'You are connected'
c.sendall(ms.encode())
while True:
        msg = c.recv(1024)
        if msg.decode() == 'exit':
                print('Connection ended')
                break
        # else:
        print(msg.decode())
        data = input('enter something..')
        c.sendall(data.encode())
        if data == 'exit':
            break
s.close()
