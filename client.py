import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 44444))
while True:
    data=s.recv(1024)
    print(data.decode())