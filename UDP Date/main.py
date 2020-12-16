import socket
from datetime import date

today = date.today()

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('localhost', 9999))


print('Server is listening')


d = s.recvfrom(1024)
print(d[0].decode())
while (True):

    s.sendto(str(today).encode(),d[1])
    command = s.recvfrom(1024)
    if command[0].decode() == "stop":
        break
    elif command[0].decode() == "continue":
        continue
s.close()
