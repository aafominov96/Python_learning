import socket as s
ip_port = (s.gethostbyname(s.gethostname()), 8888)

test_data = s.gethostname()
byte_test_data = test_data.encode()

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.connect(ip_port)
sock.send(byte_test_data)
echodata = sock.recv(1024).decode()
print("Echo: ", echodata)
sock.close()