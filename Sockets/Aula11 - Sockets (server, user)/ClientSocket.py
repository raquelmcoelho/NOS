from socket import *
cliente = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 4321
adrrserver = (host, port)
cliente.connect(adrrserver)
print("click enter")

# dinâmica
resposta = 0
while resposta != "saindo do programa :)":
    # send resposta do cliente
    enviar = input("")
    cliente.send(enviar.encode())
    # mostrar o send do server
    enviado = cliente.recv(1024)
    resposta = enviado.decode()
    print(resposta)
cliente.close()
