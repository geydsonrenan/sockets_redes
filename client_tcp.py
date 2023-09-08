from socket import *

servername = 'localhost'
serverport = 55080
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername, serverport))

while 42:
    msg = input('digite: ')
    clientsocket.send(msg.encode()) 
