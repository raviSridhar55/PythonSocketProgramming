import socket
bm = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 9999
bm.connect((hst,port))
dt = bm.recv(767)
print('Server :',dt.decode())
while True:
    gt = input('Client 2 : ')
    bm.send(gt.encode())
    if(gt=='bye'):
        break
    dt1 = bm.recv(767)
    print('Server :', dt1.decode())
bm.close()