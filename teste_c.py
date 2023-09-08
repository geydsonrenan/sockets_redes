from socket import *

name_server = "localhost"
server_port = 51001

client = socket(AF_INET, SOCK_DGRAM)
while 42:
    msg = input("Digite o nome para retornar o ip:")

    client.sendto(msg.encode(), (name_server, server_port))
    data, address = client.recvfrom(1024)

    resposta_ip = data.decode().strip()
    print(f"O ip que o DNS encontrou de {msg} foi : {resposta_ip}")

client.close()
