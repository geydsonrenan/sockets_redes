from socket import *

dns = {}

name = "localhost"
port = 51009

server = socket(AF_INET, SOCK_DGRAM)
print("Starting Server...")
server.bind((name, port))
print("Server DNS ON!")

while 42:
    msg, ip = server.recvfrom(1024)
    msg = msg.decode()
    msg = msg.split(',')
    print(msg)
    
    if msg[0] == "gravar":
        dns[msg[-2]+msg[-1]] = msg[1]+' '+msg[2]
        print(f"registrou o {msg[1]} no DNS.")
        server.sendto(f'{msg[-2]+msg[-1]} registrado com sucesso'.encode(), ip)
    
    elif msg[0] == "request":
        try:
            print('.')
            server.sendto(dns[msg[1]+msg[-1]].encode(), ip)
        except:
            print("DNS não encontrado.")
            server.sendto('Not Found'.encode(), ip)
            
    elif msg[0] == 'delete':
        del dns[msg[1]+msg[-1]]
        print(f"Endereço {msg[1]+msg[-1]} deletado do servidor.")
        server.sendto(f'Endereço {msg[1]} deletado com sucesso'.encode(), ip)
        #if dns == {}:
            #break
server.close()


