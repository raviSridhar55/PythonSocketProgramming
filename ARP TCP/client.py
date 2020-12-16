import socket

c = socket.socket()

c.connect(('localhost', 9999))

ip_address = input("Ip address-> ")
c.sendall(ip_address.encode())
mac_address = c.recv(1024)
print(mac_address.decode())
c.close()
