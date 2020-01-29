import socket as s
#ip_port = ('192.168.1.67', 8888)
ip_port = (s.gethostbyname(s.gethostname()), 8888)
test_data = s.gethostname()
byte_test_data = test_data.encode()
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.connect(ip_port)
sock.send(byte_test_data)
sock.close()
