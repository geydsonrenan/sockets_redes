from socket import *

servername = gethostname()
serverport = 55080
nome_fic = "seunomepornascimento.app"

name_dns = "localhost"
dns_port = 51009


dic_dia = {
    "01": "DO MORRO",
    "02": "DO BAILE",
    "03": "DA BEKA",
    "04": "DA NAIKE",
    "05": "DO BOREU",
    "06": "DA NET",
    "07": "DAS NOVINHAS",
    "08": "DO FUTURO",
    "09": "DA MARCAÇÃO",
    "10": "DO FACÃO",
    "11": "DA VILA",
    "12": "DA OSTENTA",
    "13": "DA PRAIA",
    "14": "DOS BRODER",
    "15": "DO ZAPZAP",
    "17": "DO FACEBUK",
    "18": "DAS PARADA",
    "19": "DO BAGUIU",
    "20": "DO PEDAÇO",
    "21": "DO CAMARO",
    "22": "DAS POSIÇÃO",
    "23": "DOS MOMENTO",
    "24": "DO ORKUT",
    "25": "DO BRINQUEDO",
    "26": "DA NOIA",
    "27": "DA ANARQUIA",
    "28": "DO ROCK",
    "29": "DAS GATINHA",
    "30": "DAS TATTO",
    "31": "DA ADIDAS",
}

dic_mes = {
    "01": "JOSE",
    "02": "BOREU",
    "03": "PIXILINGA",
    "04": "PEQUENO",
    "05": "BAGUIU",
    "06": "LEKE",
    "07": "BARÃO",
    "08": "VEI",
    "09": "ZEZIM",
    "10": "CHUREU",
    "11": "PIRIQUITO",
    "12": "MAICÃO",     
}

def conection_dns(name_serv, serv_port, dns_name, dns_port, nome_fic):
    msg = f'gravar,{name_serv},{serv_port},{nome_fic},TCP'
    sock_serv = socket(AF_INET, SOCK_DGRAM)
    sock_serv.sendto(msg.encode(), (dns_name, dns_port))
    resp, address = sock_serv.recvfrom(1024)
    print(resp.decode())
    sock_serv.close()
def conection_delete_dns(nome_fic, dns_name, dns_port):
    msg = f'delete,{nome_fic},TCP'
    sock_serv = socket(AF_INET, SOCK_DGRAM)
    sock_serv.sendto(msg.encode(), (dns_name, dns_port))
    resp, address = sock_serv.recvfrom(1024)
    print(resp.decode())
    sock_serv.close()
    
conection_dns(servername, serverport, name_dns, dns_port, nome_fic)
# mudar isso: 
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((servername, serverport))
serversocket.listen(5)
print('SERVER TCP ON!')
sck_client, address = serversocket.accept()

while 42:
    msg = sck_client.recv(1024)
    msg = msg.decode().split('/')
    try:
        resp = dic_mes[msg[1]] + ' ' + dic_dia[msg[0]]
        sck_client.send(resp.encode())
    except:
        break
serversocket.close()
conection_delete_dns(nome_fic, name_dns, dns_port) 
