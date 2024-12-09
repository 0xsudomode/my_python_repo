#!/usr/bin/python3

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1337

# connect the server
client_socket.connect((host,port))
resp = client_socket.recv(1024).decode()

print(f"server : {resp}")

# cleanup
client_socket.close()
