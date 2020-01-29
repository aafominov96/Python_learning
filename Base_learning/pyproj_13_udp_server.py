import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('192.168.1.67', 8888)
sock.bind(ip_port)
res = sock.recv(1024)
print("Message: ", res.decode('utf-8'))
sock.close()
