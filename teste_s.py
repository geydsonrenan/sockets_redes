from socket import *

dns_table = {
    "www.google.com": "192.165.1.1",
    "www.geydson.com": "192.165.1.2",
    "www.gabriel.com": "192.165.1.3",
    "www.kelvin.com": "192.165.1.4",
    "www.allyson.com": "192.165.1.5",
    "www.kiev.com": "192.165.1.6",
}

name_server = "localhost"
server_port = 51001
server = socket(AF_INET, SOCK_DGRAM)

print("Starting Server...")
server.bind((name_server, server_port))


while 42:
    sck_client, address = server.recvfrom(1024)
    sck_client = sck_client.decode()

    ip = dns_table.get(sck_client, "Not Found").encode()
    send = server.sendto(ip, address)
    # print(sck_client.decode())
