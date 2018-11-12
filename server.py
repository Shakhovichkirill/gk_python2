import json
from typing import Any, Dict
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", default="0.0.0.0")
parser.add_argument('-p', type=int, default=7777)
start_srv = parser.parse_args()
IP = start_srv.a
PORT = start_srv.p

def handle_presence(request):
    if request['user'] == {'account_name': 'test', 'status': 'Yes, I am here!'}:
        return{'response': 200}

mapping = {
    'presence': handle_presence
}

def handler(request: Dict[str, object]):
    print(f'Client sent {request}')
    response = mapping[request['action']](request)
    print(f'Response: {response}')
    return response

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((IP, PORT))
    s.listen(1)

    while True:
        client, addr = s.accept()
        with client:
            data_b = client.recv(1000000)
            data = json.loads(data_b, encoding='utf-8')
            response = handler(data)
            client.send(json.dumps(response).encode('utf-8'))