#!/usr/bin/python3

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1337

# bind a socket to the provided address
server_socket.bind((host,port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}...")

# wait for a connection
client_socket , client_address = server_socket.accept()
print(f"Connection established with {client_address[0]}")

# send a message to the connected client
client_socket.sendall(b'Welcome to the server !')

# cleanup
client_socket.close()
server_socket.close()

