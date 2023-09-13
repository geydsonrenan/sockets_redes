from socket import *
import time
tempo_inicial = time.perf_counter()

name_server = "localhost"
dns_port = 51009

anos  = ["06/10", "01/09", "19/03", "22/01", "29/12"]

def request_dns(name_server, dns_port):
    msg = f"request,{name_server},TCP"
    sock_client = socket(AF_INET, SOCK_DGRAM)
    sock_client.bind(("localhost", 53000))
    sock_client.sendto(msg.encode(), (name_server, dns_port))
    msg_resp , ip = sock_client.recvfrom(1024)
    sock_client.close()
    print(msg_resp.decode())
    return msg_resp.decode()

server_port = request_dns(name_server, dns_port)
#mudar isso:
#clientsocket = socket(AF_INET, SOCK_STREAM)

#clientsocket.connect(("localhost", int(server_port)))
#clientsocket.bind(('localhost', 53000))
messagem = "informe o ano de nascimento"
tempo_inicial = time.perf_counter()

for i in range(len(anos)):
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect(("localhost", int(server_port)))
    msg = anos[i] + '/' + 'localhost' + '/' + '53000'
    clientsocket.send(msg.encode())
    clientsocket.close()
    while 42:
        clientsocket = socket(AF_INET, SOCK_STREAM)
        clientsocket.bind(('localhost', 53000))
        clientsocket.listen(1)
        resp, address = clientsocket.accept()
        resp = resp.recv(1024)
        print(resp.decode())
        clientsocket.close()
        break
tempo_final = time.perf_counter()
print(f'tempo para resoluir as 5 requisições: {tempo_final - tempo_inicial}')
