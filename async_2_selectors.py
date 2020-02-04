# -*- coding: utf-8 -*-
import socket
import selectors    # мониторинг


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # fileobj - файловый объект, который имеет .fileno(), число
    # events - события
    # data - связанные данные (сессия, id сессии)
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()    # ждет от клиента подключения
    print('Connection from', addr)  # входящее подключение

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)  # ждет от клиента сообщения

    if request:
        response = 'Hello, World!\n'.encode()   # закодирует в bytes
        client_socket.send(response)
    else:
        selector.unregister(client_socket)  # снятия с регистрации
        client_socket.close()


def event_loop():	 # передача управления
    while True:
        events = selector.select()  # список кортежей (key, events)

        # key - SelectorKey - именованный котреж (Collections)
        # содержит fileobj, events, data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
