from socket import socket, gethostbyname
from traceback import print_exc

cs = socket() # creates a TCP/IP client socket

host = 'localhost'
hostip = gethostbyname(host)
print(hostip)
port = 8087

cs.settimeout(10)

try:
    cs.connect((hostip, port))
except Exception:
    print_exc()
else:
    print('Connection success!')
    data = cs.recv(4096)
    nowstr = str(data, 'utf-8')
    print(nowstr)
finally:
    cs.close()