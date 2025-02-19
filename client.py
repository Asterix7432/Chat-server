import socket

HEADER = 64
PORT = 5050
SERVER = ''
FORMAT = 'utf-8'
EXIT = 'exit'
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
