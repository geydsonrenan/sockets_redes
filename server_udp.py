from socket import *

name_server = 'localhost'
server_port = 51001
name_dns = "localhost"
dns_port = 51009
print('SERVER ON')

def conection_dns(name_serv, serv_port, dns_name, dns_port):
    msg = f'gravar,{name_serv},{serv_port}'
    sock_serv = socket(AF_INET, SOCK_DGRAM)
    sock_serv.sendto(msg.encode(), (dns_name, dns_port))
    sock_serv.close()
conection_dns(name_server, server_port, name_dns, dns_port)
server = socket(AF_INET, SOCK_DGRAM)
server.bind((name_server, server_port))
while 42:
    sck_client, address = server.recvfrom(1024)
    print(sck_client.decode())
