from socket import *
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a")
parser.add_argument('-p', type=int, default=7777)
start_srv = parser.parse_args()
IP = start_srv.a
PORT = start_srv.p

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((IP, PORT))
    msg = {
        "action": "presence",
        "time": 1234,
        "type": "status",
        "user": {
                "account_name":  "test",
                "status":      "Yes, I am here!"
        }
    }
    msg_str = json.dumps(msg)
    s.send(msg_str.encode('utf-8'))
    data = s.recv(1000000)
    print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной', len(data))