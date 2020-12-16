import socket

c = socket.socket(type=socket.SOCK_DGRAM)

c.connect(('localhost',9999))

ip_address = input("Ip address:")
print(" ")
c.sendto(ip_address.encode(),('localhost',9999))
mac_address=c.recvfrom(1024)
print("Your MAC address is:  " + mac_address[0].decode())

c.close()