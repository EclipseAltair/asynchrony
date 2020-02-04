#!/usr/bin
import socket
from select import select   # мониторинг изменений состояний файловых объектов и сокетов
# в unix - всё - файлы
# .fileno() - возвращает файловый дескриптор, т.е. номер файла, ассоциирующийся с конкретным файлом


to_monitor = []		# мониторинг

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()   # ждет от клиента подключения
    print('Connection from', addr)   # входящее подключение

    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)   # ждет от клиента сообщения

    if request:	# условие для прерывания цикла
        response = 'Hello, World!\n'.encode()   # закодирует в bytes
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():	 # передача управления
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])   # для чтения, для записи, ошибки

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
