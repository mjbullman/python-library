import socket
import sys


def connect(host: str, port: int) -> socket.socket:
    sock = socket.socket()
    sock.connect((host, port))
    return sock

conn = connect("192.168.1.192", 80)

print(conn.getsockname())
print(conn.getpeername())