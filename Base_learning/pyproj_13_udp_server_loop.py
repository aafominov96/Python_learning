import socket as s

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
ip_port = ('192.168.1.67', 8888)
sock.bind(ip_port)
count = 0
while True:
    try:
        res = sock.recv(1024)
        count += 1
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message from client #%f', count, res.decode('utf-8'))
