import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 44444))
s.listen(1)

conn = None
addr = None


def check_socket_connection():
  global conn,addr
  while True:
    try:
        s.getpeername()
    except:
        conn, addr = s.accept()

threading.Thread(target=check_socket_connection).start()
while True:
    try:
        message = input("İstemciye mesaj gönderin:")
        conn.sendall(bytes(message.encode()))
    except:
        break
