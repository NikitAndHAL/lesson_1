# Программа клиента, запрашивающего текущее время
from socket import *
import json
import time
import sys


try:
    addr = sys.argv[1]
except:
    addr = 'localhost'
try:
    port = int(sys.argv[2])
except:
    port = 7777


def receive(message_b):
    message_json = message_b.decode('utf-8')
    message = json.loads(message_json)
    return message


def send_to(message):
    message_json = json.dumps(message)
    message_b = message_json.encode('utf-8')
    return message_b


s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((addr, port))   # Соединиться с сервером

presence_message = {
    'action': 'presence',
    'time': time.time(),
    'type': 'status',
    'user': {
        'account_name': input('Введите имя: '),
        'status': "What's up",
    }
}
login_message = {
    'action': 'authenticate',
    'time': time.time(),
    'user': {
        'account_name': 'QWERTY',
        'password': 'qwerty',
    }
}

probe_message = {
    'action': 'probe'
}
msg_message = {
    'action': 'msg'
}
quit_message = {
    'action': 'quit'
}
join_message = {
    'action': 'join'
}
leave_message = {
    'action': 'leave'
}

s.send(send_to(presence_message))
tm = receive(s.recv(1024))            # Принять не более 1024 байтов данных
s.close()
print("response: %s" % tm)

