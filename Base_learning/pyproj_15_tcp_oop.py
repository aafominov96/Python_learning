import socketserver as ss
import socket as s

class TCP_oop_server(ss.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print("Adress: {}".format(self.client_address))
        print("Data: {}".format(data.decode()))
        self.request.sendall(data+b' - all cool')
if __name__ == '__main__':
    ip_port = (s.gethostbyname(s.gethostname()), 8888)
    with ss.TCPServer(ip_port, TCP_oop_server) as serv:
        serv.serve_forever()
