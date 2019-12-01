from socket import socket
from datetime import datetime

ss = socket() # TCP/IP socket
host = 'localhost'
port = 8087

ss.bind((host, port))
print('Server successfully binded on port {0}'.format(port))

ss.listen(10)

while True:
    print('Waiting for client connections...')
    sock, address = ss.accept() # blocking call

    # sock - New socket on the server machine that knows how to communicate with the client whose request was accepted
    # address - Address of the client (remote machine)
    print('Connection accepted')
    print(address)

    datetime = datetime.now()
    nowstr = datetime.strftime('%d-%B,%Y-%H:%M')
    sock.sendall(bytes(nowstr, 'utf-8'))