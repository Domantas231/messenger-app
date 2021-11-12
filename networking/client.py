import socket
import json
from networking.database import save_message

HEADER = 16
PORT = 5050 # don't forget port-forwarding
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "" # enter your server adress
ADDR = (SERVER, PORT)
CONFIRMATION_MESSAGE = "!RECEIVED"

# TODO change the send message function so that
# its made up of 3 different ones where:
# connecting, sending and disconnecting

def send_message(msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def send(msg, sender, receiver):
        msg_json = { 'sender' : sender, 'message' : msg, 'receiver' : receiver }

        msg_json = json.dumps(msg_json)

        message = msg_json.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))

        client.send(send_length)
        client.send(message)

        recv_length = int(client.recv(HEADER).decode(FORMAT))
        recv_msg = client.recv(recv_length).decode(FORMAT)

        # to reduce clutter
        if recv_msg == CONFIRMATION_MESSAGE:
            save_message(sender, msg)

        print(recv_msg)

    send(DISCONNECT_MESSAGE)
