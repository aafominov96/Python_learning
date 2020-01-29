import os
import socket as s

unix_socket_name = 'unix_file.sock'

sock = s.socket(s.AF_UNIX, s.SOCK_DGRAM)

if os.path.exists(unix_socket_name):
    os.remove(unix_socket_name)

sock.bind(unix_socket_name)

while True:
    try:
        res = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print("Message: ", res.decode('utf-8'))

