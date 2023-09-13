from socket import *

name_server = "localhost"
dns_port = 51009

anos  = ["06/10", "01/09", "19/03", "22/01", "29/12"]

def request_dns(name_server, dns_port):
    msg = f"request,{name_server}, UDP"
    sock_client = socket(AF_INET, SOCK_DGRAM)
    sock_client.bind(("localhost", 52000))
    sock_client.sendto(msg.encode(), (name_server, dns_port))
    msg_resp , ip = sock_client.recvfrom(1024)
    sock_client.close()
    print(msg_resp.decode())
    return msg_resp.decode()

server_port = request_dns(name_server, dns_port)
print("Server On")

client = socket(AF_INET, SOCK_DGRAM)
messagem = "informe o ano de nascimento"

client.bind(("localhost", 52000))
client.sendto(anos[0].encode(), (name_server, int(server_port)))
resp, ip = client.recvfrom(1024)
print(resp.decode())
client.close()
