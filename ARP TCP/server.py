# ARP implementation using UDP
import socket
import getmac
s = socket.socket()
s.bind(('localhost', 9999))
s.listen(1)
c, addr = s.accept()
print('Connected with ', addr)
data = c.recv(1024)
ip_address = data.decode()


mac = getmac.get_mac_address(ip=ip_address)

if mac is not None:
    c.sendall(mac.encode())
else:
    c.sendall("Not found".encode())

s.close()
