import socketserver as ss
import socket as s

class UDP_oop_server(ss.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        print('Adress:{}'.format(self.client_address[0]))
        print('Format:{}'.format(data.decode()))

with ss.UDPServer((s.gethostbyname(s.gethostname()), 8888), UDP_oop_server) as serv:
    serv.serve_forever()