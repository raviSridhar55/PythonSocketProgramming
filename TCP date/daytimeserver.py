import socket
from datetime import datetime

today = datetime.today()

s = socket.socket()
s.bind(('localhost', 9999))

s.listen(1)
print('Server is listening')

c, addr = s.accept()
print('Connected with ', addr)
d = c.recvfrom(1024)
while (True):
    #data = input("Enter message:")
    c.sendall(str(today).encode())
    command = c.recvfrom(1024)
    if command[0].decode() == "stop":
        break
    elif command[0].decode() == "continue":
        continue
s.close()
