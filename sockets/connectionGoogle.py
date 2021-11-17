#Example script to connect to Google using socket
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket succefully created")
except  socket.error as e:
    print("socket creation failed with error " + e)

#default port for socket
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

#connectiong to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")
print("on port " + host_ip)
