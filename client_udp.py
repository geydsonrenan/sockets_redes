from socket import *

name_server = 'localhost'
server_port = 51001
client = socket(AF_INET, SOCK_DGRAM)
messagem = input('Digite:')
client.sendto(messagem.encode(), (name_server, server_port))
client.close()