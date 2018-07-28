from sys import argv
from socket import socket, setdefaulttimeout, AF_INET, SOCK_STREAM

*, timeout, host, port_check = argv
setdefaulttimeout(float(timeout))
sock = socket(AF_INET, SOCK_STREAM)
isopen_port = sock.connect_ex((host, int(port_check)))
print 'port %s OOOOOOOPENNNNNN'%(port_check) if isopen_port == 0 else 'port %s NET_MTF'%(port_check)
