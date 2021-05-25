from socket import *

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect(("127.0.0.1", 9998))

print(cliente.recv(4096).decode())
cliente.send(input().encode())

print(cliente.recv(4096).decode())
cliente.send(input().encode())

print("Seu imc é: ", cliente.recv(4096).decode())

cliente.close()
