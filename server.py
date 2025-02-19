import socket
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR  = (SERVER,PORT)
FORMAT = 'utf-8'
EXIT = 'exit'



#creating the server (type/family of the socket, how the data is sent over the connection)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f'[NEW CONNCETION] {addr} CONNECTED')
    connected = True
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(HEADER).decode(FORMAT) 
            if msg == EXIT:
                connected = False
            print(f'{addr} {msg}')


def start():
    server.listen()
    print(f'[LISTENING] server is listeing on  {SERVER}')
    while True:
        conn ,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')
print('[STARTING] The server is starting')
start()
