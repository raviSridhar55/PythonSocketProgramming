import socket
jk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 7868
jk.connect((hst,port))
dt = jk.recv(767)
print('Server said :',dt.decode())
while True:
    gt = input('Client 1: ')
    jk.send(gt.encode())
    if(gt=='end'):
        break
    dt1 = jk.recv(767)
    print('Server:', dt1.decode())
jk.close()