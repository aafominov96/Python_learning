import socket as s

unix_socket_name = 'unix_file.sock'
sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
sock.sendto(b"Hop, hey, lalalay", unix_socket_name)
