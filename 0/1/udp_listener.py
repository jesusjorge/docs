import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("", 12345))
while True:
    data, addr = sock.recvfrom(65536)
    print("[" + addr[0] + "] " + data.decode())

