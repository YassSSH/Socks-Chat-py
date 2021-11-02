import socket

HOST = (
    (
            [
                ip
                for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                if not ip.startswith("127.")
                if not ip.startswith("172.")
                if not ip.startswith("10.")
                if not "197." in ip
                if not "56." in ip
            ]
            or [
                [
                    (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                    for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                ][0][1]
            ]
    )
)[0]
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(3)

while True:
    communication_socket, address = server.accept()
    notif = input(f'U received a message from {address} do u want to see it ? (y/n) :')
    if notif == "y" or "yes" :
        message = communication_socket.recv(1024).decode('utf-8')
        print(f"Message : {message}")
        communication_socket.send(f"Got ur message".encode('utf-8'))
        re = input("Voulez-vous repondre ? (y/n) :")
        if re == "y" or "yes" :
            communication_socket.send(input("Entrez votre message : ").encode('utf-8'))
        else:
            communication_socket.close()
            print(f"Session rompu avec {address}")
    else:
        communication_socket.close()
        print(f"Session rompu avec {address}")

