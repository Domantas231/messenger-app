import socket
import threading
import json

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 16
DISCONNECT_MESSAGE = "!DISCONNECT"
CONFIRMATION_MESSAGE = "!RECEIVED"
VERIFICATION_MESSAGE = "!VERIFY"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg_json = conn.recv(msg_length).decode(FORMAT)

            msg = json.loads(msg_json)

            if msg['message'] == DISCONNECT_MESSAGE and msg['receiver'] == 'SERVER':
                connected = False

            print(f"[{addr}] Author: {msg['sender']} Message: {msg['message']} Receiver: {msg['receiver']}")
            send(CONFIRMATION_MESSAGE, conn)

    conn.close()

def send(msg, conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    conn.send(send_length)
    conn.send(message)

def start():
    server.listen()
    print(f"[LISTENING] Listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()