import socket

from _thread import *
def thrd(con):
    con.send(str.encode('Welcome to srvr \n'))
    while True:
        c = con.recv(245)
        print('clnt :', c.decode())
        gt = input('server : ')
        if c.decode() == 'bye':
            con.send(gt.encode())
            print('connection ended')
            break
        gt = input('server : ')
        con.send(gt.encode())
    con.close()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 9999
Th_cnt = 0
s.bind((hst, port))
print('waiting for connection..............')
s.listen(7)
while True:
    con,adr = s.accept()
    print('Connected to :', adr[0], ":", adr[1])
    start_new_thread(thrd,(con,))
    Th_cnt += 1
    print("Thread No: "+str(Th_cnt))

s.close()



