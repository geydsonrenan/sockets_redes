from socket import *

servername = 'localhost'
serverport = 55080
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((servername, serverport))
serversocket.listen(5)

while 42:
    sck_client, address = serversocket.accept()
    while 42:
        msg = sck_client.recv(1024)
        print(msg.decode())
