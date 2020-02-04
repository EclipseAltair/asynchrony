#!/usr/bin
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()   # блокирующая функция (ждет от клиента подключения)
    print('Connection from', addr)   # входящее подключение

    while True:
        '''
        Внутри этого цикла не можем принимать подключения новых клиентов
        '''
        request = client_socket.recv(4096)   # блокирующая функция (ждет от клиента сообщения)

        if not request:   # условие для прерывания цикла
            break
        else:
            response = 'Hello, World!\n'.encode()   # закодирует в bytes
            client_socket.send(response)

    client_socket.close()
