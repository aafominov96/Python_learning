import socket as s

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
site = 'example.com'
sock.connect((site, 80))
http_zapros =[
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n']
content = '\n'.join(http_zapros)
print('Сообщение, отправленное на сервер ', http_zapros[1])
print(content)
print('Конец сообщения')
sock.send(content.encode())
result = sock.recv(10000)
print('Ответ сервера: ')
print(result.decode())
