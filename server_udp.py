from socket import *

name_server = 'localhost'
server_port = 51001
server = socket(AF_INET, SOCK_DGRAM)
server.bind((name_server, server_port))
print('SERVER ON')

while 42:
    sck_client, address = server.recvfrom(1024)
    print(sck_client.decode())