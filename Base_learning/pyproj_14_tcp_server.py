import socket as s

#ip_port = ('192.168.1.67', 8888)
ip_port = (s.gethostbyname(s.gethostname()), 8888)
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.bind(ip_port)
sock.listen(5)
sock.setblocking(False)
#sock.settimeout(5)
while True:
    try:
        client, adr = sock.accept()
    except s.error:
        print("Wait")
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        client.setblocking(True)
        print("Message: ", client.recv(1024).decode('utf-8'), '    from adress: ', adr)
        client.close()