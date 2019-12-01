from socket import socket
from time import sleep
from threading import Thread
from multiprocessing import Process

ss = socket() # TCP/IP socket
host = 'localhost'
port = 8091

quotes = [
    'Honesty is best policy',
    'Try try till u succed',
    'No quote'
]

class HandlerThread(Process):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        sock = self.sock
        data = sock.recv(4096)
        choice = int(str(data, 'utf-8'))
        quote = quotes[choice-1]
        sleep(10)

        sock.sendall(bytes(quote, 'utf-8'))

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

    thread = HandlerThread(sock)
    thread.start()