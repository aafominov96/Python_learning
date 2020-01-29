import socket as s

sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
#ip_port = ('192.168.1.67', 8888)
ip_port = (s.gethostbyname(s.gethostname()), 8888)
test_data = s.gethostname()
byte_test_data = test_data.encode()
#sock.sendto(b'Data:', ip_port)
sock.sendto(byte_test_data, ip_port)
