import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)
clientSocket, clientAddress = sock.accept()

clientName = clientSocket.recv(1024).decode()

while True:
    command = input("{}: ".format(clientName))
    clientSocket.send(command.encode())
    if command.lower() == "exit":
        break
    results = clientSocket.recv(1024).decode()
    print(results)

clientSocket.close()
sock.close()
