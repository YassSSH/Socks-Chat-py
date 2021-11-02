import socket


HOST = "192.168.1.24"
PORT = 5001

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send(input("Entrez votre message :").encode('utf-8'))
print(socket.recv(1024))