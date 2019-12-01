from socket import socket as socketfn
import socket

cs = socketfn(type=socket.SOCK_DGRAM)
cs.sendto(bytes('Lets go for fire drill', 'utf-8'), (socket.gethostbyname('localhost'), 9000))