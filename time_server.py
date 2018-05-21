# Программа сервера времени
from socket import *
import time
import json
import sys


port, addr = 7777, ''
try:
    key = sys.argv[1]
    if key == '-p':
        port = int(sys.argv[2])
    elif key == '-a':
        addr = sys.argv[2]
except:
    pass

try:
    key = sys.argv[3]
    if key == '-p':
        port = int(sys.argv[5])
    elif key == '-a':
        addr = sys.argv[5]
except:
    pass

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((addr, port))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # одновременно обслуживает не более
                                  # 5 запросов.


def receive(message_b):
    message_json = message_b.decode('utf-8')
    message = json.loads(message_json)
    return message


def send_to(message):
    message_json = json.dumps(message)
    message_b = message_json.encode('utf-8')
    return message_b


clients_online = []
while True:
    client, addr = s.accept()     # Принять запрос на соединение
    print(type(client))
    print("Получен запрос на соединение от %s" % str(addr))
    hello_message = receive(client.recv(1024))
    clients_online.append(hello_message)
    print(clients_online[0])
    response = {
        'responce': '200',
        'alert': 'Добро пожаловать!'
    }
    
    # Обратите внимание, дальнейшая работа ведётся с сокетом клиента
    client.send(send_to(response))   # <- По сети должны передаваться байты,
                                           # поэтому выполняется кодирование строки 
    client.close()

