from socket import socket as socketfn
import socket

ss = socketfn(type=socket.SOCK_DGRAM)
ss.bind(('127.0.0.1', 9000))

data, address = ss.recvfrom(4096)
print(str(data, 'utf-8'))
print(address)