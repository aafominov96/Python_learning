import socket as s

sock = s.socket(s.AF_INET, s.SOCK_STREAM)
site = 'iu.bmstu.ru'
sock.connect((site, 80))
http_zapros =[
    'GET / HTTP/1.1',
    'Host: iu.bmstu.ru',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n']
content = '\n'.join(http_zapros)
print('Сообщение, отправленное на сервер ', http_zapros[1])
print(content)

print('Конец сообщения')
while True:
    sock.send(content.encode())
result = sock.recv(200000)
print('Ответ сервера: ')
print(result.decode())
