import socket
c=socket.socket()
c.connect(('localhost',9999))
print('Client waiting for connection')
while(True):
    data=input("Enter message:")
    c.sendall(data.encode())
    msg=c.recv(1024)
    print("Server echoed:"+msg.decode())
    if (msg.decode()=='stop'):
        print('Stopping connetion')
        break
c.close()