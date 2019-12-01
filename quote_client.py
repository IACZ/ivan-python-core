from socket import socket, gethostbyname
from traceback import print_exc

cs = socket() # creates a TCP/IP client socket

host = 'localhost'
hostip = gethostbyname(host)
port = 8091

choice = input('Enter number between 1 - 3: ')

try:
    cs.connect((hostip, port))
except Exception:
    print_exc()
else:
    print('Connection success!')
    cs.sendall(bytes(choice, 'utf-8'))

    data = cs.recv(4096)
    quote = str(data, 'utf-8')
    print(quote)
finally:
    cs.close()