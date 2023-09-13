from socket import *

name_server = 'localhost'
server_port = 51001

name_dns = "localhost"
dns_port = 51009

print('SERVER ON')

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
    sck_client = sck_client.decode().split("/")
    msg = dic_mes[sck_client[1]] + " " + dic_dia[sck_client[0]]
    server.sendto(msg.encode(), address)    
