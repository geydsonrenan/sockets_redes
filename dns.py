from socket import *

dns = {}

name = "localhost"
port = 51009

server = socket(AF_INET, SOCK_DGRAM)
print("Starting Server...")
server.bind((name, port))
print("Server ON")

while 42:
    msg, ip = server.recvfrom(1024)
    msg = msg.decode()
    msg = msg.split(',')
    
    if msg[0] == "gravar":
        dns[msg[1]] = msg[2]
        print(ip)
        print(f"registrou o {msg[1]} no DNS")
        print(dns)
    else:
        msg[0] == "search"
        if msg[1] in dns:
            print(dns[msg[1]])
        else:
            print("DNS não encontrado")
        
