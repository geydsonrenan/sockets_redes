from socket import *
import time

name_server = "localhost"
dns_port = 51009
endereco_requisitado = "seunomepornascimento.app"

anos = ["06/10", "01/09", "19/03", "22/01", "29/12"]

def request_dns(name_server, dns_port):
    msg = f"request,{name_server},UDP"
    sock_client = socket(AF_INET, SOCK_DGRAM)
    sock_client.sendto(msg.encode(), ('localhost', dns_port))
    msg_resp , ip = sock_client.recvfrom(1024)
    sock_client.close()
    if msg_resp.decode() == 'Not Found':
        print(msg_resp.decode())
        return None, None
    resp = msg_resp.split()
    print(resp[0].decode())
    return resp[1].decode(), resp[0].decode()

server_port, host = request_dns(endereco_requisitado, dns_port)
if server_port != None:
    print("Client UDP ON")
    client = socket(AF_INET, SOCK_DGRAM)
    tempo_inicial = time.perf_counter()

    for i in range(len(anos)):
        msg = anos[i] + '/' + f'{len(anos)-i-1}'
        tem_incial = time.perf_counter()
        client.sendto(msg.encode(), (host, int(server_port)))
        resp, ip = client.recvfrom(1024)
        temp_final = time.perf_counter()
        print(f'O tempo da requisição {i} foi: {temp_final-tem_incial} segundos')
        print(resp.decode())
    client.close()

    tempo_final = time.perf_counter()
    print(f'tempo para resoluir as 5 requisições: {tempo_final - tempo_inicial} segundos')
else:
    print('Não foi possível acessar o endereço pois ele não possui accessos no Server DNS')

