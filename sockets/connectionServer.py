#importing the socket library
import socket

#creation of the socket object
s = socket.socket()

#reserving a port on the PC
port = 12345

s.bind(('127.0.0.1', port))
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

#a forever loop until we interrupt it or
#an error occurs
while True:
    
    #Establish connection with client
    c, addr = s.accept()
    print("Got connection from", addr)
    
    #send a thank you message to the client. encoding to send byte type
    c.send('thank you for connecting'.encode())
    
    #Close the connection with the client
    c.close()

    #Breaking once connection closed
    break